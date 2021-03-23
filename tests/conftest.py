import pytest

from dirtree_cli.command_dispatcher import CommandDispatcher
from dirtree_cli.dir_composite import Directory


@pytest.fixture(scope='function')
def command_dp():
    return CommandDispatcher()


@pytest.fixture(scope='function')
def directory():
    return Directory()
