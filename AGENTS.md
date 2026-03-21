# AGENTS.md

## Cursor Cloud specific instructions

### Project overview

`akzept` is a batch Python project that generates curated awesome-style Markdown reference lists from Zotero library exports. There are **no running services** (no web server, database, or Docker containers). The "application" is two Python scripts that transform JSON into Markdown.

### Python version

The project requires **Python >= 3.14** (`pyproject.toml`). The VM's system Python is 3.12, so Python 3.14 is installed from the deadsnakes PPA (`ppa:deadsnakes/ppa`, package `python3.14`). The virtualenv at `.venv` uses Python 3.14.

### Virtual environment

```
source /workspace/.venv/bin/activate
```

### Running the scripts

Both scripts require Zotero export files in the `exports/` directory (gitignored). Create sample data there if none exists.

- `python scripts/zotero_to_awesome.py` — reads `exports/aprt-snapshot-*.json`, outputs awesome-style Markdown. Supports `--category-whitelist-file config/awesome-category-whitelist.txt`.
- `python scripts/build_list.py` — reads `exports/aprt-*.csljson`, outputs `LIST.md`.

### Lint

```
ruff check scripts/
```

### Key caveats

- The `exports/` directory is gitignored and will be empty on a fresh clone. Both scripts will error if no matching export files exist. Create sample JSON files in `exports/` to test.
- `build_list.py` overwrites `LIST.md` in the repo root. Run `git checkout -- LIST.md` afterwards if you don't want to commit test output.
- Neither script uses `pyzotero` at runtime (they only use stdlib `json`/`pathlib`/etc.), but `pyzotero` is the declared project dependency in `pyproject.toml`.
