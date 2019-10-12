# Python Project Template

## Overview

This is a minimal template for a typical Python application developed in Visual Studio Code. It includes a folder structure and boilerplate for:

* A CLI app
* Python module code
* Tests
* Makefile

As well as a VS Code settings file to integrate a virtual environment and testing framework.

## Installation

1. Create a new environment by running `python3 -m venv .venv`
2. Activate the virtual environment (Command Pallete > Python: Create Terminal in VS Code)
3. Execute `pip3 install -r requirements.txt`

## Contents

```
├── .vscode
│   └── settings.json
├── app
│   └── main.py
├── .env
├── .git
├── .gitignore
├── Makefile
├── Readme.md
├── python_project
│   └── functions.py
├── requirements.txt
└── tests
    └── test_it.py
```

### .vscode

#### settings.json

VS Code settings that:

* Specifies .venv/bin/python as the `pythonPath` 
* Specifies pytest as the testing framework
* Launches pytest with verbose output and ignores the .venv folder
* Enables linting

### app

A dedicated folder for a CLI app.

#### main.py

A boilerplate [Click](https://click.palletsprojects.com/en/7.x/) program.

### python_project

Python module code.

#### functions.py

Initial module code.

### tests

Unit tests.

#### test_it.py

Initial test code.

### Additional Files

#### .env

VS Code environment variables. Sets the `PYTHONPATH` to the root folder.

#### .gitignore

#### Makefile

Includes a PHONY rule for cleaning up Python artifacts.

#### Readme

This document

#### requirements.txt

Python package requirerments. Includes:

* pytest
* pylint
* click