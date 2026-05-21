# Cookiecutter Template

A [Cookiecutter](https://cookiecutter.readthedocs.io/en/stable/README.html) template for Python packages using modern tooling.

## Included Tools

| Function                       | Tool                | Link                                         |
|--------------------------------|---------------------|----------------------------------------------|
| Package management             | uv                  | https://docs.astral.sh/uv/                   |
| Build backend                  | Hatchling           | https://hatch.pypa.io/latest/                |
| Documentation                  | Zensical            | https://zensical.com/                        |
| Documentation: theme           | Material for MkDocs | https://squidfunk.github.io/mkdocs-material/ |
| Documentation: auto docstrings | mkdocstrings-python | https://mkdocstrings.github.io/python/       |
| Task automation                | Nox                 | https://nox.thea.codes/en/stable/            |
| Testing                        | pytest              | https://docs.pytest.org/                     |
| Linting                        | ruff                | https://docs.astral.sh/ruff/                 |
| Formatting                     | ruff                | https://docs.astral.sh/ruff/                 |
| Type checking                  | ty                  | https://docs.astral.sh/ty/                   |
| Import sorting                 | isort               | https://pycqa.github.io/isort/               |
| Pre-commit hooks               | pre-commit          | https://pre-commit.com/                      |
| Documentation: publish         | GitHub Actions      | https://docs.github.com/en/actions           |
| PyPI: publish                  | GitHub Actions      | https://docs.github.com/en/actions           |

## Getting Started

With `cookiecutter` and `uv` installed:

```bash
cookiecutter https://github.com/chris-santiago/cookie.git
```

Complete the prompts, then:

```bash
cd <your-project>
conda env create -f environment.yml
conda activate <your-env-name>
uv sync
git init
pre-commit install
```

## uv Quickstart

### Add a dependency

```bash
uv add numpy
```

### Add a dev dependency

```bash
uv add --group dev pytest
```

### List dependencies

```bash
uv tree
```

### Run a command in the project environment

```bash
uv run pytest
```

### Lock and sync

```bash
uv lock
uv sync
```

For more, see the [uv documentation](https://docs.astral.sh/uv/).
