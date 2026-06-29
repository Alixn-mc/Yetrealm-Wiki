#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python -m pip install -r requirements.txt
python tools/audit_wiki.py
python -m mkdocs build --strict
echo "Build passed. The wiki project is valid."
