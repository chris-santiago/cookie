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

### Pyproject.toml

We've moved much of the metadata and package options to the `pyproject.toml` file, which is inherently declarative. This also means we don't use a `requirements.txt` file; users should list their package requirements in the `pyproject.toml` file, under the `[project]dependencies=` section.

We've also consolidated configuration files (pytest.ini, .pylintrc, etc) into the `pyproject.toml` file.

**Note:** Flake8 doesn't support `pyproject.toml`, so its configuration is set during invocation. Arguments are found in the `.pre-commit-config.yaml` and `noxfile.py` files.

## Noxfile

The Noxfile will run several tests and commands:

- Pytest in current Python environment
- Pytest in all supported Python environments
- Mypy
- Pylint
- Flake8
- iSort
- Black
- Check-manifest
- Pre-commit trailing-whitespace
- Pre-commit end-of-file-fixer
- Pre-commit check-yaml
- Sphinx-apidoc
- Sphinx-build

Pytest coverage lands in ./htmlcov
Documentation lands in ./docs/build and ./docs/source

### Nox Configuration

By default, the command `nox` will run sessions under the `"pytest"` and `"qa"` tags.  These include: Pytest in current Python environment, Mypy, Pylint, Flake8, iSort, Black and Pre-commit trailing-whitespace/end-of-file-fixer/check-yaml.

Example:

```bash
> nox

nox > Ran multiple sessions:
nox > * test_system_python: success
nox > * mypy: success
nox > * pylint: success
nox > * flake8: success
nox > * isort: success
nox > * black: success
nox > * precommit: success
```

#### Other Tags

The `quick` tag will run Pytest in current Python environment and Flake8.

Example:

```bash
> nox -t quick

nox > Ran multiple sessions:
nox > * test_system_python: success
nox > * flake8: success
```

The `pytest` tag will run Pytest in current Python environment, only.

Example:

```bash
> nox -t pytest

nox > Session test_system_python was successful.
```

The `tests` tag will run Pytest in all supported Python environments.

Example:

```bash
> nox -t tests

nox > Ran multiple sessions:
nox > * test_supported_python-3.8: success
nox > * test_supported_python-3.9: success
```

The `pre-release` tag runs all sessions, including documentation build, but **excluding** Pytest in the current Python environment (it will test all supported environments, instead).

Example:

```bash
> nox -t pre-release

nox > Ran multiple sessions:
nox > * test_supported_python-3.8: success
nox > * test_supported_python-3.9: success
nox > * mypy: success
nox > * pylint: success
nox > * flake8: success
nox > * isort: success
nox > * black: success
nox > * manifest: success
nox > * precommit: success
nox > * docs: success
```

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

#### Quick initialization
We've included an `init.sh` file to quickly install your project (editable), update and install pre-commit.

- Navigate to your project's directory (i.e. `cd yourdirectoryhere`).
- Run `bash init.sh`

#### Manual initialization

Alternatively, you can complete these same steps one-by-one.  Omit `pre-commit`, if desired.

- Navigate to your project's directory (i.e. `cd yourdirectoryhere`).
- Install project in editable mode, with dev requirements: `pip install -e. [docs,tests,qa,build]`.
- Initialize project as a git repo: `git init`.
- Install pre-commit: `pre-commit install`.
- Add files and commit: `git add --all`, `git commit -m "inital"`.
    - You may need to re-run both commands if the pre-commit fixers make changes to your files.
- Run nox: `nox`

```bash
> cd yourproject
> pip install -e ."[dev]"
> git init
> pre-commit autoupdate
> pre-commit install
```

#### First commit:

If you're usinging pre-commit, your first commit will look something like this:

```bash
> git add --all
> git commit -m "initial"

trim trailing whitespace.................................................Passed
fix end of files.........................................................Passed
check yaml...............................................................Passed
check for added large files..............................................Passed
debug statements (python)................................................Passed
isort....................................................................Passed
black....................................................................Passed
flake8...................................................................Passed
```

#### First Nox run:

The first `nox` run is fairly quick as we're not creating any separate test environment, by default.  However, the first time you run the `tests` or `pre-release` tag will take some time as new environments are build; subsequent runs will be much faster as we reuse these virtual (conda) environments, by default.

You'll see **a lot** of output:

```bash
> nox

nox > Running session test_system_python
nox > pytest
nox > Session test_system_python was successful.
nox > Running session mypy
nox > mypy --install-types --non-interactive -p python_project
Success: no issues found in 2 source files
...
...
...
nox > Ran multiple sessions:
nox > * test_system_python: success
nox > * mypy: success
nox > * pylint: success
nox > * flake8: success
nox > * isort: success
nox > * black: success
nox > * precommit: success
```
