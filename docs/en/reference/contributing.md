# Contributing and Maintenance

Yetrealm Wiki is maintained from source-backed data and public release notes.

## Contribution Rules

- Keep English and Chinese pages aligned at the section level when possible.
- Keep game IDs visible.
- Use screenshots that show the actual item, structure, UI, or boss clearly.
- Run `mkdocs build --strict` before submitting changes.

## Local Build

```bash
pip install -r requirements.txt
mkdocs build --strict
```

## GitHub Pages

The site deploys from `main` through GitHub Actions. After a successful push, GitHub Pages updates the public site at:

`https://alixn-mc.github.io/Yetrealm-Wiki/`

