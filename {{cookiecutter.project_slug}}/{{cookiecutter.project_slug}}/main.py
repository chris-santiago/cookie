import argparse

from {{cookiecutter.project_slug}}.hello_world import hello_world


def get_parser():
    """Get ArgumentParser instance."""
    parser = argparse.ArgumentParser(description='Print Hello World')
    return parser


def run(parser):
    """Run from CLI."""
    hello_world()
