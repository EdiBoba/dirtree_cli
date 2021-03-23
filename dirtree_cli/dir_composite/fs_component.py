from abc import ABC, abstractmethod


class FileSystemComponent(ABC):
    """
    Base class for all file system items
    """
    _name: str

    @abstractmethod
    def to_string(self, level=0):
        pass
