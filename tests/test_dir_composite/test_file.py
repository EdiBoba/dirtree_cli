from dirtree_cli.dir_composite import File


def test_file():
    file = File('filename')

    assert file._name == 'filename'
    assert file.to_string(1) == '\tfilename'
    assert file.to_string(2) == '\t\tfilename'
