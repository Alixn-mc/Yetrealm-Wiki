# Validation Report

Repository target:

```text
Alixn-mc/Yetrealm-Wiki
```

Expected Pages URL:

```text
https://alixn-mc.github.io/Yetrealm-Wiki/
```

Build command executed during packaging:

```bash
mkdocs build --strict
```

Result:

```text
PASS
```

Validated items:

- `mkdocs.yml` exists at repository root.
- `.github/workflows/pages.yml` exists.
- `docs/index.md` exists.
- All files referenced in the MkDocs navigation exist.
- MkDocs Material dependency is declared in `requirements.txt`.
- Local strict build completes successfully.

Notes:

- Do not upload through GitHub's web uploader when publishing the full package; use GitHub Desktop or Git.
- The `site/` folder is intentionally not included. GitHub Actions will build it automatically.
