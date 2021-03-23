import pathlib

import pytest

from dirtree_cli.command_dispatcher.exceptions import UnknownCommandError


def test_unknown_command(command_dp):
    with pytest.raises(UnknownCommandError):
        command_dp.execute('NOTACOMMAND')


def test_command_with_wrong_args(command_dp):
    with pytest.raises(TypeError):
        command_dp.execute('LIST no way')


def test_execute_from_file(command_dp):
    file_path = pathlib.Path(__file__).parent.parent / 'commands.txt'
    command_dp.execute(f"EXEC {file_path}")
    assert command_dp.execute("list") == f"""\
{pathlib.Path().cwd()}\r
\tfoods\r
\t\tfruits\r
\t\tgrains\r
\t\tvegetables\r
\t\t\tsquash"""
