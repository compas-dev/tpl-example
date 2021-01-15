# COMPAS Example template

Cookietcutter template for COMPAS examples.

[Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/readme.html#)
is a command-line utility that lets you quickly bootstrap a new project from a template.
It takes a directory tree and copies it into your new project,
replacing all the generic info that finds surrounded by templating tags `{{` and `}}` with your project info written in `cookiecutter.json`.

## Features

* Example directory and file structure

## What's included

* `script.py`
* `doc.rst`
* `environment.yml`

## Requirements

Install `cookiecutter` command line: `pip install cookiecutter`

## Usage

In the terminal, go to the folder where you want to place your project:

```bash
cd path/to/project/parent
```

Generate a new Cookiecutter template layout:

```bash
cookiecutter gh:compas-dev/tpl-example
```
