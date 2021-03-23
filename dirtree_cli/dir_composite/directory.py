import pathlib

from .fs_component import FileSystemComponent
from .exceptions import ExistError, NotExistError


class Directory(FileSystemComponent):
    """
    Represents a directory in file system.

    Directory may contains child directories.
    """
    _parent: 'Directory'
    _child: dict
    _abs_path: str

    def __init__(self, dir_name: str = None, parent: 'Directory' = None):
        """
        Initialized directory object.

        If init without arguments -> directory name = cwd.

        :param dir_name: name of directory
        :param parent: parent directory for this directory
        """
        if dir_name is None:
            cwd = pathlib.Path.cwd()
            self._name = str(cwd.parts[-1])
            self._abs_path = str(cwd.parent.resolve())
        else:
            self._name = dir_name
            self._abs_path = str(pathlib.Path(parent._abs_path) / parent._name)
        self._parent = parent
        self._child = {}

    def _get_dir_dict(self, operation, path, *args) -> dict:
        """
        Returns a dictionary in which there may be a directory

        :param operation: current operation
        :param path: path to current file
        :param args: pathlib.Path(path).parts
        :return: dict with directories
        :raises: NotExistError if parent directory not exist
        """
        if len(args) == 1:
            return self._child
        else:
            if args[0] in self._child:
                return self._child[args[0]]._get_dir_dict(operation, path, *args[1:])
            else:
                raise NotExistError(operation, path, args[0])

    def make_dir(self, directory_path: str) -> None:
        """
        Creates directory.

        :param directory_path: path to directory
        :return: None
        :raises: NotExistError if parent directory not exist
        :raises: ExistError if directory exist
        """
        path_parts = pathlib.Path(directory_path).parts
        dir_dict = self._get_dir_dict('create', directory_path, *path_parts)
        if path_parts[-1] in dir_dict:
            raise ExistError('create', directory_path, path_parts[-1])

        dir_dict[path_parts[-1]] = Directory(path_parts[-1], self)
        dir_dict[path_parts[-1]].update_abs_path()

    def delete_dir(self, directory_path: str):
        """
        Deletes directory

        :param directory_path: path to directory
        :return: None
        :raises: NotExistError if parent directory not exist
        :raises: NotExistError if directory not exist
        """
        path_parts = pathlib.Path(directory_path).parts
        dir_dict = self._get_dir_dict('delete', directory_path, *path_parts)
        if path_parts[-1] not in dir_dict:
            raise NotExistError('delete', directory_path, path_parts[-1])
        dir_dict.pop(path_parts[-1])

    def rename_dir(self, directory_path, new_name) -> None:
        """
        Renames directory

        :param directory_path: path to directory
        :param new_name: new name of the directory
        :return: None
        :raises: NotExistError if parent directory not exist
        :raises: NotExistError if directory not exist
        :raises: ExistError if directory with new_name exist
        """
        path_parts = pathlib.Path(directory_path).parts
        dir_dict = self._get_dir_dict('rename', directory_path, *path_parts)
        if path_parts[-1] not in dir_dict:
            raise NotExistError('rename', directory_path, path_parts[-1])
        if new_name in dir_dict:
            raise ExistError('rename', directory_path, new_name)
        dir_dict[new_name] = dir_dict.pop(path_parts[-1])
        dir_dict[new_name]._name = new_name
        dir_dict[new_name].update_abs_path()

    def update_abs_path(self) -> None:
        """
        Updates absolute links ti directories

        :return: None
        """
        self._abs_path = f"{self._parent._abs_path}/{self._name}"
        for child_dir in self._child.values():
            child_dir.update_abs_path()

    def to_string(self, level=0) -> str:
        """
        Recursively creates string to print directory

        :param level: nesting level
        :return: str
        """
        sorted_components = sorted(self._child)
        result = ''
        if level:
            result += '\r\n' + '\t' * level + self._name
        else:
            result += str(pathlib.Path(self._abs_path) / self._name)
        for item in sorted_components:
            result += self._child[item].to_string(level + 1)
        return result

    def move_dir(self, from_path, to_path) -> None:
        """
        Moves directory to another directory

        :param from_path: the path from where move
        :param to_path: the path where move
        :return: None
        """
        from_path_parts = pathlib.Path(from_path).parts
        to_path_parts = pathlib.Path(to_path).parts
        from_dir_dict = self._get_dir_dict('move', from_path, *from_path_parts)
        if from_path_parts[-1] not in from_dir_dict:
            raise NotExistError('move', from_path, from_path_parts[-1])

        to_dir_dict = self._get_dir_dict('move', to_path, *to_path_parts)
        if to_path_parts[-1] not in to_dir_dict:
            raise NotExistError('move', to_path, to_path_parts[-1])

        value = from_dir_dict.pop(from_path_parts[-1])
        to_dir_dict[to_path_parts[-1]]._child[value._name] = value
