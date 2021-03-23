from typing import Optional

from ..dir_composite import Directory
from .exceptions import UnknownCommandError


class CommandDispatcher:
    """
    This class executes executes commands from user and file, returns
    help message about commands
    """
    _cwd: Directory
    _commands: dict

    def __init__(self):
        """
        Initialize dispatcher with current working directory.

        Establish a correspondence between commands and directory functions.
        """
        self._cwd = Directory()
        self._commands = {
            'help': self.get_help,
            'create': self._cwd.make_dir,
            'list': self._cwd.to_string,
            'move': self._cwd.move_dir,
            'delete': self._cwd.delete_dir,
            'rename': self._cwd.rename_dir,
            'exec': self.execute_from_file
        }

    def execute(self, command: str) -> Optional[str]:
        """
        Executes a single command.

        :param command: command with arguments
        :type command: str
        :return: None if command is completed
        :rtype: None
        :raises: UnknownCommandError if command not in self._commands
        """
        arguments = command.lower().strip('\r\n ').split(' ')
        command = arguments.pop(0)
        func = self._commands.get(command)
        if not func:
            raise UnknownCommandError(command)
        try:
            return func(*arguments)
        except TypeError:
            raise TypeError(f"Can't execute command {command} "
                            f"with arguments {arguments}")

    def execute_from_file(self, file_name: str) -> None:
        """
        Executes all commands from file.

        :param file_name: file to read commands
        :return: None if command is completed
        """
        with open(file_name) as file:
            for command in file:
                try:
                    result = self.execute(command)
                    if result:
                        print(result)
                except Exception as exc:
                    print(exc)

    @staticmethod
    def get_help() -> str:
        """
        :return: prints help string for commands
        :rtype: str
        """
        return """\
HELP - show help for commands.
LIST - show all files and directories in current directory
CREATE <dir_name> - create directory.
MOVE move/from/here> move/to/here - move directory to another directory
DELETE this/directory - delete directory
RENAME this/directory new_name - rename directory
EXEC path/to/file.txt - execute all commands from file"""
