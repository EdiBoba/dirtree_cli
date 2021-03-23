# DirTree CRUD CLI client

![Python version](https://img.shields.io/badge/Python-3.6--3.9-blue)
![Coverage](https://img.shields.io/badge/Coverage-92%25-brightgreen)


Cli-client that provides work with folders like a REST api

## Key Features

* Provides simple API
* Easy to use
* OS independent

## How it works

* dir_composite imitate work with file system without side effects like create directories
* command_dispatcher translates commands to directory functions

Other ways to solve this task:

* production way: command dispatcher translate commands to pathlib and os functions (work with real file system)
* non-production way without side effects: create a TemporaryDirectory (from tempfile module), 
this directory to execute pathlib and os functions, after close program created temporary directory and all its contents are removed from the filesystem

## Requirements

* [Python](https://www.python.org/) >= 3.6

## Usage

Run cli client:
```
$ python run_client.py
```

View commands help:
```
>>> HELP
```

Create a new directory in current working directory:
```
>>> CREATE some_directory
```

Create a new subdirectory:
```
>>> CREATE some_directory/subdirectory
```

List of all files and directories in current working directory:
```
>>> LIST
```

Move some directory to another directory:
```
>>> MOVE some_directory/subdirectory to_directory
```

Delete a directory:
```
>>> DELETE some_directory/subdirectory
```

Rename a directory:
```
>>> RENAME some_directory/subdirectory
``` 

Execute all commands from file (file must exist)
```
>>> EXEC path/to/file
```

## Run in docker

Build image:
```shell
docker build -t dirtree-cli .
```

Run application:
```shell
docker run -i --rm --name dirtree dirtree-cli
```