# Cookiecutter Template

[Cookiecutter](https://cookiecutter.readthedocs.io/en/stable/README.html) is command-line utility 
that creates projects from cookiecutters (project templates), e.g. creating a Python package project 
from a Python package project template.

- Documentation: [https://cookiecutter.readthedocs.io](https://cookiecutter.readthedocs.io)
- GitHub: [https://github.com/cookiecutter/cookiecutter](https://github.com/cookiecutter/cookiecutter)

## PDM 

This cookie assumes that you've installed PDM via these [instructions](https://pdm.fming.dev/latest/#update-the-pdm-version)

The `post_gen_project.sh` hook can be modified to install PDM in virtual environment via pip, if
desired (though not recommended).

## Included Tools

| Function                       | Tool                | Link                                         |
|--------------------------------|---------------------|----------------------------------------------|
| Dependency management          | PDM                 | https://pdm.fming.dev/latest/                |
| Documentation                  | MkDocs              | https://www.mkdocs.org/                      |
| Documentation: theme           | Material for MkDocs | https://squidfunk.github.io/mkdocs-material/ |
| Documentation: auto docstrings | mkdocstrings-python | https://mkdocstrings.github.io/python/       |
| Automated testing              | Nox                 | https://nox.thea.codes/en/stable/index.html  |
| Testing                        | pytest              | https://docs.pytest.org/en/7.3.x/            |
| Linting                        | ruff                | https://beta.ruff.rs/docs/                   |
| Type checking                  | Pyright             | https://microsoft.github.io/pyright/#/       |
| Formatting                     | Black               | https://black.readthedocs.io/en/stable/      |
| Automated QA                   | pre-commit          | https://pre-commit.com/                      |
| QA                             | isort               | https://pycqa.github.io/isort/               |
| QA                             | check-manifest      | https://github.com/mgedmin/check-manifest    |
| Linting                        | SQLFluff            | https://www.sqlfluff.com/                    |

## Getting Started

Using a Python environment with `cookiecutter` installed, run:

`cookiecutter https://github.cloud.capitalone.com/lno127/cookie.git`

and complete the prompts.

```bash
cd <your project dir>
conda env create -f environment.yml
conda activate <your env name>
pdm install
git init
pre-commit install
```

~~This cookie executes a post-generation script (`hooks/post_gen_project.sh`) that will:

1. Create a virtual environment via Conda
2. Install all development dependencies in your virtual environment
3. Install your project (editable) in your virtual environment
4. Initialize a git repo in your new project directory
5. Install pre-commit in your repo~~

## PDM Quickstart

As installed via this cookie, PDM will automatically detect the Conda virtual environment and operate
within. See [Working with Virtual Environments](https://pdm.fming.dev/latest/usage/venv/) for other
options.

Here are a few commands to get you started. For much more, see the [CLI Reference](https://pdm.fming.dev/latest/reference/cli/)
or [Manage Dependencies](https://pdm.fming.dev/latest/usage/dependency/) guide.

### Add a required dependency

`pdm add <package>`

Example: `pdm add numpy`


### Add a development dependency

`pdm add -d <package>`

Example: `pdm add -d flake8`


### Add a development dependency into a specific group

`pdm add -dG <group name> <package>`

Example: `pdm add -dG qa flake8`

### List Dependencies

`pdm list`

### List Dependencies as Graph

`pdm list --graph`

### Export Dependencies

`pdm export -o requirements.txt`