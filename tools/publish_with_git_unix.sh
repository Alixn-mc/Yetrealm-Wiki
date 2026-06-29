#!/usr/bin/env bash
set -euo pipefail
REPO_URL="https://github.com/Alixn-mc/Yetrealm-Wiki.git"
TARGET="$HOME/Desktop/Yetrealm-Wiki"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

if [ -d "$TARGET/.git" ]; then
  cd "$TARGET"
  git pull origin main
else
  git clone "$REPO_URL" "$TARGET"
fi

rsync -a --delete --exclude='.git' --exclude='site' "$ROOT/" "$TARGET/"
cd "$TARGET"
git add .
git commit -m "Initial official Yetrealm Wiki" || true
git push origin main

echo "Push completed. Now open GitHub Settings > Pages and choose GitHub Actions."
