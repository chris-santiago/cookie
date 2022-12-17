import sys

import nox

nox.options.sessions = ["test_system_python"]
nox.options.tags = ["qa"]

PROJECT = "{{cookiecutter.project_slug}}"
PYTHON_REQUIRES = "{{cookiecutter.python_version}}"
PYTHON_SYS = f"{sys.version_info.major}.{sys.version_info.minor}"


def python_versions(max_version=None):
    """Get a list of Python versions to test."""
    if not max_version:
        max_version = PYTHON_SYS
    return [
        f"3.{v}"
        for v in range(
            int(PYTHON_REQUIRES.rsplit(".", 1)[-1]),
            int(max_version.rsplit(".", 1)[-1]) + 1,
        )
    ]


@nox.session(
    venv_backend="conda",
    python=python_versions(),
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
    session.install("pytest", "pytest-cov")
    session.install(".")
    session.run("pytest")


@nox.session(reuse_venv=True, tags=["quick"])
def test_system_python(session):
    """Run unit tests in current Python environment."""
    session.install("pytest", "pytest-cov")
    session.install(".")
    session.run("pytest")


@nox.session(python=False, tags=["qa"])
def mypy(session):
    """Run static type-checking on source code."""
    session.run("mypy", "--install-types", "--non-interactive", "-p", PROJECT)


@nox.session(python=False, tags=["qa"])
def pylint(session):
    """Lint code using Pylint."""
    session.run("pylint", PROJECT, "--verbose")


@nox.session(python=False, tags=["qa", "quick"])
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


@nox.session(python=False, tags=["qa"])
def isort(session):
    """Fix module imports."""
    session.run("isort", ".")


@nox.session(python=False, tags=["qa"])
def isort(session):
    """Format code with Black."""
    session.run("black", PROJECT)


@nox.session(python=False, tags=["qa"])
def precommit(session):
    """Run Pre-Commit fixers and checks."""
    session.run("check-manifest")
    session.run("pre-commit", "run", "trailing-whitespace", "--files", "*.py")
    session.run("pre-commit", "run", "end-of-file-fixer", "--files", "*.py")
    session.run("pre-commit", "run", "check-yaml", "--all-files")


@nox.session(python=False, tags=["docs", "pre-release"])
def docs(session):
    """Build package documentation."""
    session.run("sphinx-apidoc", "--separate", "-f", PROJECT, "-o", "docs/source/")
    session.run("sphinx-build", "-b", "html", "docs/source/", "docs/build/html")
