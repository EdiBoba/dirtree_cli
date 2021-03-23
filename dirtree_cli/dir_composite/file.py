from .fs_component import FileSystemComponent


class File(FileSystemComponent):
    """
    Represents a single file in file system
    """
    def __init__(self, file_name: str):
        self._name = file_name

    def to_string(self, level: int = 0) -> str:
        """
        Returns file name with indentations

        :param level: nesting level
        :return: file name with indentations for print
        """
        return '\t' * level + self._name
