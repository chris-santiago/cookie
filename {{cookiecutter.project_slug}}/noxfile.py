import nox

nox.options.default_venv_backend = "uv"


@nox.session
def tests(session):
    session.run("uv", "sync", "--all-extras", "--all-groups", external=True)
    session.run("uv", "run", "pytest", "-n", "auto", *session.posargs, external=True)


@nox.session(python=False)
def lint(session):
    session.run("uvx", "ruff", "check", "src/{{cookiecutter.project_slug}}", "--fix", external=True)
    session.run("uvx", "ruff", "format", "src/{{cookiecutter.project_slug}}", external=True)


@nox.session(python=False)
def type_check(session):
    session.run("uvx", "ty", "check", "src/{{cookiecutter.project_slug}}", external=True)


@nox.session()
def build(session: nox.Session) -> None:
    session.run("uv", "build", external=True)


@nox.session
def docs(session: nox.Session) -> None:
    session.run("uv", "run", "zensical", "build", external=True)
