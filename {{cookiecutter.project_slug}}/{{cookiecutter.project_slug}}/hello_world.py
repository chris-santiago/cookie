"""Hello world module."""

def hello_world(msg: str = 'Hello World.') -> str:
    """Return hello world."""
    return msg


def hello_world_cli(*args):
    """Return hello world."""
    return list(args)
