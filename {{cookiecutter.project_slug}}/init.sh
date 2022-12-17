# for project initialization
pip install -e ."[dev]" && \
git init && \
pre-commit autoupdate && \
pre-commit install
