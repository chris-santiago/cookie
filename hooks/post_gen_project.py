import shutil
import os
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
        cleanup(['{{cookiecutter.project_slug}}/main.py'])

    if '{{cookiecutter.test_multiple_versions}}' == 'yes':
        cleanup(['noxfile.py'])
        os.rename('multi_noxfile.py', 'noxfile.py')


if __name__ == '__main__':
    main()
