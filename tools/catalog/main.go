// Command catalog builds the catalog using the same ZIP encoding as the service.
package main

import (
	"archive/zip"
	"bytes"
	"crypto/sha256"
	"encoding/hex"
	"encoding/json"
	"flag"
	"fmt"
	"io/fs"
	"os"
	"path/filepath"
	"sort"
	"time"

	"gopkg.in/yaml.v3"
)

type item struct {
	ID      string `json:"id"`
	Version string `json:"version"`
	Path    string `json:"path"`
	SHA256  string `json:"sha256"`
}
type manifest struct {
	Schema  string `yaml:"schema"`
	ID      string `yaml:"id"`
	Version string `yaml:"version"`
}

func main() {
	if err := run(); err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
}
func run() error {
	check := flag.Bool("check", false, "verify catalog.json without modifying it")
	out := flag.String("out-dir", "", "optional directory for generated validation ZIPs")
	flag.Parse()
	dirs, err := os.ReadDir(".")
	if err != nil {
		return err
	}
	var items []item
	seen := map[string]bool{}
	for _, d := range dirs {
		if !d.IsDir() {
			continue
		}
		raw, err := os.ReadFile(filepath.Join(d.Name(), "adapter.yaml"))
		if os.IsNotExist(err) {
			continue
		}
		if err != nil {
			return err
		}
		var m manifest
		if err = yaml.Unmarshal(raw, &m); err != nil {
			return err
		}
		if m.Schema != "gaia.connection-adapter/v1" || m.ID == "" || m.Version == "" || seen[m.ID] {
			return fmt.Errorf("invalid or duplicate manifest: %s", d.Name())
		}
		seen[m.ID] = true
		var names []string
		err = filepath.WalkDir(d.Name(), func(p string, e fs.DirEntry, err error) error {
			if err != nil {
				return err
			}
			if e.IsDir() {
				return nil
			}
			if !e.Type().IsRegular() {
				return fmt.Errorf("regular files only: %s", p)
			}
			names = append(names, p)
			return nil
		})
		if err != nil {
			return err
		}
		sort.Strings(names)
		var b bytes.Buffer
		z := zip.NewWriter(&b)
		for _, name := range names {
			raw, err = os.ReadFile(name)
			if err != nil {
				return err
			}
			rel, err := filepath.Rel(d.Name(), name)
			if err != nil {
				return err
			}
			h := &zip.FileHeader{Name: filepath.ToSlash(rel), Method: zip.Deflate}
			h.SetModTime(time.Date(1980, 1, 1, 0, 0, 0, 0, time.UTC))
			h.SetMode(0644)
			w, err := z.CreateHeader(h)
			if err != nil {
				return err
			}
			if _, err = w.Write(raw); err != nil {
				return err
			}
		}
		if err = z.Close(); err != nil {
			return err
		}
		sum := sha256.Sum256(b.Bytes())
		items = append(items, item{m.ID, m.Version, d.Name(), hex.EncodeToString(sum[:])})
		if *out != "" {
			if err = os.MkdirAll(*out, 0755); err != nil {
				return err
			}
			if err = os.WriteFile(filepath.Join(*out, d.Name()+".zip"), b.Bytes(), 0644); err != nil {
				return err
			}
		}
	}
	if len(items) == 0 {
		return fmt.Errorf("no adapter packages found; run from repository root")
	}
	data, err := json.MarshalIndent(struct {
		Schema   string `json:"schema"`
		Packages []item `json:"packages"`
	}{"gaia.connection-catalog/v1", items}, "", "  ")
	if err != nil {
		return err
	}
	data = append(data, '\n')
	if *check {
		old, err := os.ReadFile("catalog.json")
		if err != nil {
			return err
		}
		if !bytes.Equal(old, data) {
			return fmt.Errorf("catalog.json is stale; run go run ./tools/catalog")
		}
	} else if err = os.WriteFile("catalog.json", data, 0644); err != nil {
		return err
	}
	fmt.Printf("Validated catalog: %d packages\n", len(items))
	return nil
}
