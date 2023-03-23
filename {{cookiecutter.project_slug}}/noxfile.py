import sys

import nox

nox.options.tags = ["pytest", "qa"]  # default tags to run using command `nox`

PROJECT = "{{cookiecutter.project_slug}}"
SUPPORTED_PYTHON = [{{cookiecutter.python_requires}}]


@nox.session(
    venv_backend="conda",
    python=SUPPORTED_PYTHON,
    reuse_venv=True,
    tags=["tests", "pre-release"],
)
def test_supported_python(session):
    """
    Run unit tests in separate Python environments, from `MIN_PYTHON` to `CURR_PYTHON` versions.

    Notes
    -----
    Comment this session out if you don't require testing with other Python versions.

    Uses Conda backend, by default.
    """
    session.install(".[tests]")
    session.run("pytest")


@nox.session(python=False, tags=["quick", "pytest"])
def test_system_python(session):
    """Run unit tests in current Python environment."""
    session.run("pytest")


@nox.session(python=False, tags=["qa", "pre-release"])
def isort(session):
    """Fix module imports."""
    session.run("isort", ".")


@nox.session(python=False, tags=["qa", "pre-release"])
def black(session):
    """Format code with Black."""
    session.run("black", PROJECT)


@nox.session(python=False, tags=["qa", "pre-release"])
def mypy(session):
    """Run static type-checking on source code."""
    session.run("mypy", "--install-types", "--non-interactive", "-p", PROJECT)


@nox.session(python=False, tags=["qa"])
def pylint(session):
    """Lint code using Pylint."""
    session.run("pylint", PROJECT, "--verbose", "--fail-under", PYLINT_REQUIRES)


@nox.session(python=False, tags=["qa", "quick", "pre-release"])
def flake8(session):
    """Lint code using Flake8."""
    session.run(
        "flake8",
        PROJECT,
        "--count",
        "--statistics",
        "--select=E9,F63,F7,F82",
        "--show-source",
    )  # these fail
    session.run(
        "flake8", PROJECT, "--count", "--statistics", "--exit-zero"
    )  # these warn


@nox.session(python=False, tags=["pre-release"])
def manifest(session):
    """Check distribution manifest."""
    session.run("check-manifest", ".")


@nox.session(python=False, tags=["docs", "pre-release"])
def docs(session):
    """Build package documentation."""
    session.run("sphinx-apidoc", "--separate", "-f", PROJECT, "-o", "docs/source/")
    session.run("sphinx-build", "-b", "html", "docs/source/", "docs/build/html")


@nox.session(python=False, tags=["build", "pre-release"])
def dependencies(session):
    session.run(
        "pip-compile",
        "--output-file=requirements.txt",
        "pyproject.toml",
        "--resolver=backtracking",
    )
