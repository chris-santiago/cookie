import sys

import nox

PROJECT = "{{cookiecutter.project_slug}}"
MIN_PYTHON = "3.7"
CURR_PYTHON = f"{sys.version_info.major}.{sys.version_info.minor}"


def python_versions():
    """Get a list of Python versions to test."""
    return [
        f"3.{v}"
        for v in range(
            int(MIN_PYTHON.rsplit(".", 1)[-1]), int(CURR_PYTHON.rsplit(".", 1)[-1])
        )
    ]


@nox.session(venv_backend="conda", python=python_versions(), reuse_venv=True)
def test_other(session):
    """
    Run unit tests in separate Python environments, from `MIN_PYTHON` to `CURR_PYTHON` versions.

    Notes
    -----
    Comment this session out if you don't require testing with other Python versions.

    Uses Conda backend, by default.
    """
    session.install("pytest", "pytest-cov")
    session.install(".")
    session.run("pytest")


@nox.session(reuse_venv=True)
def test_current(session):
    """Run unit tests in current Python environment."""
    session.install("pytest", "pytest-cov")
    session.install(".")
    session.run("pytest")


@nox.session(python=False)
def typing(session):
    """Run static type-checking on source code."""
    session.run("mypy", "--install-types", "--non-interactive", "-p", PROJECT)


@nox.session(python=False)
def qa(session):
    """Run QA code checks."""
    session.run("isort", ".")
    session.run("black", PROJECT)
    session.run("pylint", PROJECT, "--verbose")
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
    session.run("check-manifest")
    session.run("pre-commit", "run", "trailing-whitespace", "--files", "*.py")
    session.run("pre-commit", "run", "end-of-file-fixer", "--files", "*.py")
    session.run("pre-commit", "run", "check-yaml", "--all-files")


@nox.session(python=False)
def docs(session):
    """Build package documentation."""
    session.run("sphinx-apidoc", PROJECT, "-o", "docs/source/")
    session.run("sphinx-build", "-b", "html", "docs/source/", "docs/build/html")
