"""
This module imitate work with directories without side effect
in real file system.

Directories saves in Directory composite (tree like view) and commands
executes by command dispatcher which translate command to directory function.
"""
__version__ = "1.0.0"


from .main import main
from . import dir_composite
from . import command_dispatcher

__all__ = (
    'main',
    'dir_composite',
    'command_dispatcher'
)
