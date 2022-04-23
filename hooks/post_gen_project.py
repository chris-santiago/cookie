import shutil
from pathlib import Path
from typing import List


def cleanup(paths: List[str]) -> None:
    """Remove unnecessary files and directories."""
    for file_or_folder in paths:
        if Path(file_or_folder).is_dir():
            shutil.rmtree(file_or_folder)
        else:
            Path(file_or_folder).unlink(missing_ok=True)


def main():
    """Run hooks."""
    if '{{cookiecutter.cli_tool}}' == 'no':
        cleanup(['main.py'])
