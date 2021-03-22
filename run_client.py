import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).parent.resolve()))


if __name__ == '__main__':
    from dirtree_cli import main
    main()
