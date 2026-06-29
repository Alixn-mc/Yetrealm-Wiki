# Yetrealm Wiki

Official Wiki project for **Yetrealm**, built with **MkDocs Material** and deployed to **GitHub Pages**.

Live URL after deployment:

```text
https://alixn-mc.github.io/Yetrealm-Wiki/
```

## Quick publish

Use GitHub Desktop:

1. Clone `Alixn-mc/Yetrealm-Wiki`.
2. Copy this project into the cloned repository root.
3. Commit to `main`.
4. Push.
5. In GitHub repository settings, set **Pages → Source** to **GitHub Actions**.
6. Wait for the `Deploy Yetrealm Wiki` workflow to finish.

See `00_READ_ME_FIRST.md` for the full Chinese guide.

## Local preview

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
mkdocs serve
```

## Local validation

```bash
pip install -r requirements.txt
python tools/audit_wiki.py
mkdocs build --strict
```

Or run:

```text
tools/check_build.bat
```

## Project structure

```text
.github/workflows/pages.yml  GitHub Pages deployment workflow
docs/                         Wiki content and assets
mkdocs.yml                    MkDocs configuration
requirements.txt              Python dependencies
tools/                        Local validation and optional publish helpers
```

## Maintenance

When Yetrealm updates, start from `docs/reference/maintenance-playbook.md`, keep player-facing pages and reference pages in sync, then run the local validation command before committing. GitHub Actions will rebuild the site automatically after pushing to `main`.
