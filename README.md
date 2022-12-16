# Cookiecutter Template

## Important Template Changes

### Nox vs Tox
We use [nox](https://nox.thea.codes/en/stable/), rather than tox, to automate our test and build commands. We made this switch for a few reasons:

1. Nox is configured using a Python file, rather than an ini file.
2. Nox supports Conda virtual environments.
    - This means that we can create a Python 3.x environment for testing on the fly, so users don't have to separately download and install Python interpreters.
    - We can setup test environments letting Conda manage dependencies (pip is also still available).
3. We can run arbitary commands in separate virtual environments **and** the current Python environment. This reduces space consumed by virtual environments. Tox creates a virtual environment for every command, meaning separate linting, formatting, build-checks, docs, and test commands would each have their own, separate environment.
4. We can automate documentation builds in our *current* Python environment, vice a virtual environment, meaning that our docs will build in our package/docs folder, rather than the .tox/venv/ folder.
5. We can remove `Makefiles` (an issue for Windows users) and run the commands in `noxfile.py`.

### Setup.cfg vs Setup.py

We've moved much of the metadata and package options to the `setup.cfg` file, which is inherently declarative. This also means we don't use a `requirements.txt` file; users should list their package requirements in the `setup.cfg` file, under the `[options]install_requires=` section.

We've also consolidated configuration files (pytest.ini, .pylintrc, etc) into the `setup.cfg` file.

## Noxfile

The Noxfile will run several tests and commands:

- Pytest in current Python environment
- Pylint
- Flake8
- Mypy
- Sphinx-apidoc
- Sphinx-build
- Check-manifest
- iSort
- Pre-commit trailing-whitespace
- Pre-commit end-of-file-fixer

Pytest coverage lands in ./htmlcov
Documentation lands in ./docs/build and ./docs/source

## Installation

### Setup a new environment

We'll setup a new Python environment using Conda, then install cookiecutter and initialize our
Python3 project template.

```bash
conda create --name myNewEnvironment python=3.9
conda activate myNewEnvironment
conda install cookiecutter
cookiecutter https://github.com/chris-santiago/cookie.git
```

### Initialize Project

You'll be greeted with a series of prompts; most are self-explanatory. Note that cookiecutter will
create a new project directory using your response to the `project_slug` prompt.

### Install Project

- Navigate to your project's directory (i.e. `cd yourdirectoryhere`).
- Install project in editable mode, with dev requirements: `pip install -e. [docs,tests,qa,build]`.
- Initialize project as a git repo: `git init`.
- Install pre-commit: `pre-commit install`.
- Add files and commit: `git add --all`, `git commit -m "inital"`.
    - You may need to re-run both commands if the pre-commit fixers make changes to your files.
- Run nox: `nox`

```bash
cd yourproject
pip install -e .[docs,tests,qa,build]
git init
pre-commit autoupdate
pre-commit install
git add --all
git commit -m "initial"
nox
```

You'll see **a lot** of output:

```bash
nox > Running session test_prod_python
nox > Re-using existing conda env at .nox/test_prod_python.
nox > python -m pip install pytest pytest-cov
nox > python -m pip install .
nox > pytest
...
...
...
nox > Session docs was successful.
nox > Ran multiple sessions:
nox > * test_prod_python: success
nox > * test_current: success
nox > * lint: success
nox > * qa: success
nox > * docs: success
```
