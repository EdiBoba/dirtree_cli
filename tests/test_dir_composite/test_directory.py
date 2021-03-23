import pathlib

import pytest

from dirtree_cli.dir_composite import Directory
from dirtree_cli.dir_composite.exceptions import NotExistError, ExistError


def test_creation_empty():
    directory = Directory()
    cwd = pathlib.Path().cwd()
    assert directory._name == cwd.parts[-1]
    assert directory._abs_path == str(cwd.parent.resolve())
    assert directory._parent is None

    child_directory = Directory('child', directory)
    assert child_directory._name == 'child'
    assert child_directory._abs_path == str(cwd.resolve())
    assert child_directory._parent is directory


def test_make_dir(directory):
    directory.make_dir('subdirectory')
    directory.make_dir('subdirectory/some_dir')
    assert 'subdirectory' in directory._child
    assert 'some_dir' in directory._child['subdirectory']._child

    with pytest.raises(NotExistError):
        directory.make_dir('not_child/some_dir')

    with pytest.raises(ExistError):
        directory.make_dir('subdirectory')


def test_delete_dir(directory):
    directory.make_dir('a')
    directory.make_dir('a/b')
    directory.make_dir('a/c')

    directory.delete_dir('a/b')
    assert 'b' not in directory._child['a']._child
    directory.delete_dir('a')
    assert 'a' not in directory._child

    with pytest.raises(NotExistError):
        directory.delete_dir('not_exist')


def test_rename_directory(directory):
    directory.make_dir('a')
    directory.make_dir('a/b')

    directory.rename_dir('a/b', 'not_b')
    assert 'b' not in directory._child['a']._child
    assert 'not_b' in directory._child['a']._child

    directory.rename_dir('a', 'not_a')
    assert 'a' not in directory._child
    assert 'not_a' in directory._child
    assert 'not_b' in directory._child['not_a']._child

    with pytest.raises(NotExistError):
        directory.rename_dir('not_exist', 'new_name')

    with pytest.raises(ExistError):
        directory.rename_dir('not_a', 'not_a')


def test_move_directory(directory):
    directory.make_dir('a')
    directory.make_dir('b')

    directory.move_dir('b', 'a')

    assert 'b' not in directory._child
    assert 'b' in directory._child['a']._child

    with pytest.raises(NotExistError):
        directory.move_dir('not_exist', 'a')

    with pytest.raises(NotExistError):
        directory.move_dir('a', 'not_exist')