# COMPAS Example template

This project automates the set up of a new example for the COMPAS framework using an opinionated Cookiecutter template.

[Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/readme.html#)
is a command-line utility that lets you quickly bootstrap a new project from a template.
It takes a directory tree and copies it into your new project,
replacing all the generic info that finds surrounded by templating tags `{{` and `}}` with your project info written in `cookiecutter.json`.

## Features

* Example directory and file structure

## What's included

* `{{cookiecutter.example_name}}.py`
* `{{cookiecutter.example_name}}.rst`
* `environment_osx.yml`
* `environment_win.yml`

## Requirements

Install `cookiecutter` command line: `pip install cookiecutter`

## Usage

In the terminal, go to the folder where you want to place your project:

```bash
cd <your-projects-folder>
```

Generate a new Cookiecutter template layout:

```bash
cookiecutter gh:compas-dev/cookiecutter-pypackage
```

Go to project folder:

```bash
cd <project-slug>
```

## Additional settings

## License
