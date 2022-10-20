#!/usr/bin/env python
import sys
import yaml
import subprocess

from tqdm.auto import tqdm

manifest_fn = "sota_manifest.yaml"
data_registry_s3 = "s3://compassionai/data-registry"
pub_s3 = "s3://compassionai/public/data-registry"

with open("sota_manifest.yaml", 'r') as f:
    manifest = yaml.safe_load(f)

for section, entries in manifest.items():
    for entry in tqdm(entries, desc=section):
        return_code = subprocess.call(
            f"aws s3 sync --delete {data_registry_s3}/{section}/{entry} {pub_s3}/{section}/{entry}", shell=True)
        if not return_code == 0:
            sys.exit(return_code)
