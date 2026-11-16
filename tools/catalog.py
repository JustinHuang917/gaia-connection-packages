#!/usr/bin/env python3
"""Build the catalog from sorted, length-prefixed UTF-8 package contents."""
import argparse
import hashlib
import json
from pathlib import Path
import stat
import sys
import zipfile

import yaml


def package_files(directory):
    files = {}
    for path in sorted(directory.rglob('*')):
        mode = path.lstat().st_mode
        if stat.S_ISDIR(mode):
            continue
        if not stat.S_ISREG(mode):
            raise ValueError(f'regular files only: {path}')
        files[path.relative_to(directory).as_posix()] = path.read_bytes()
    return files


def content_digest(files):
    digest = hashlib.sha256()
    for name, data in sorted(files.items()):
        digest.update(name.encode('utf-8') + b'\0')
        digest.update(str(len(data)).encode('ascii') + b'\0')
        digest.update(data)
    return digest.hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--out-dir', type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    items, seen = [], set()
    for directory in sorted(root.iterdir()):
        manifest = directory / 'adapter.yaml'
        if not directory.is_dir() or not manifest.is_file():
            continue
        files = package_files(directory)
        data = yaml.safe_load(files['adapter.yaml'])
        if (not isinstance(data, dict) or data.get('schema') != 'gaia.connection-adapter/v1'
                or not isinstance(data.get('id'), str) or not data['id']
                or not isinstance(data.get('version'), str) or not data['version']
                or data['id'] in seen):
            raise ValueError(f'invalid or duplicate manifest: {directory.name}')
        guide = files.get('SKILL.md', b'').decode('utf-8')
        parts = guide.split('---', 2)
        meta = yaml.safe_load(parts[1]) if len(parts) == 3 and not parts[0].strip() else None
        if (not isinstance(meta, dict) or meta.get('name') != data['id']
                or not meta.get('description') or len(guide.encode('utf-8')) > 4096):
            raise ValueError(f'invalid or missing SKILL.md: {directory.name}')
        for name, content in files.items():
            if name.startswith('references/') and (not name.endswith('.md') or len(content) > 16384):
                raise ValueError(f'invalid reference: {directory.name}/{name}')
        operations = json.loads(files['schemas/operations.json'])
        for name, operation in operations.items():
            if not all(operation.get(key) for key in ('title', 'description', 'effect', 'input_schema')):
                raise ValueError(f'incomplete operation description: {directory.name}/{name}')
        seen.add(data['id'])
        items.append(dict(id=data['id'], description=data.get('description', ''), version=data['version'], path=directory.name,
                          sha256=content_digest(files)))
        if args.out_dir:
            args.out_dir.mkdir(parents=True, exist_ok=True)
            with zipfile.ZipFile(args.out_dir / (directory.name + '.zip'), 'w') as archive:
                for name, content in sorted(files.items()):
                    info = zipfile.ZipInfo(name, (1980, 1, 1, 0, 0, 0))
                    info.external_attr = (stat.S_IFREG | 0o644) << 16
                    archive.writestr(info, content, compress_type=zipfile.ZIP_DEFLATED)
    if not items:
        raise ValueError('no adapter packages found')
    output = (json.dumps(dict(schema='gaia.connection-catalog/v1', packages=items),
                         ensure_ascii=False, indent=2) + '\n').encode('utf-8')
    target = root / 'catalog.json'
    if args.check:
        if target.read_bytes() != output:
            raise ValueError('catalog.json is stale; run python3 tools/catalog.py')
    else:
        target.write_bytes(output)
    print(f'Validated catalog: {len(items)} packages')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, yaml.YAMLError) as error:
        print(error, file=sys.stderr)
        sys.exit(1)
