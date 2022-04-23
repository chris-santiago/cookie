import argparse

from {{cookiecutter.project_slug}}.hello_world import hello_world_cli


def get_parser():
    """Get ArgumentParser instance."""
    parser = argparse.ArgumentParser(description='Print Hello World')
    return parser


def run(parser: argparse.ArgumentParser):
    """Run from CLI."""
    args = parser.parse_args()
    hello_world_cli(args)

