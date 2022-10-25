# Esmerald

- The requirements are located in `requirements.txt` and you can locally run `make requirements`.
It will install the dev requirements as well.
- Uses cookiecutter to generate the template project
- [Esmerald](https://esmerald.dymmond.com/) is used for the tests with [pytest](https://docs.pytest.org/en/latest/)

Comes with some pre-built routes, gateways, apps, includes and an additional `serve.py` used for development purposes.

## Table of Contents

---
- [Esmerald](#esmerald)
    - [Table of Contents](#table-of-contents)
    - [Overview](#overview)
    - [Requirements](#requirements)
    - [How to install](#how-to-install)
    - [Run locally](#run-locally)
    - [Settings](#settings)
    - [Run tests](#run-tests)
    - [OpenAPI](#openapi)
---

## Overview

This is a simple cookiecutter that helps spinning up esmerald apps for your own use cases and fast.

This also helps you to understand possible folder structures that can be helpul in terms of organisation.

## Requirements

- Python 3.7 or above
- (Optional) Virtualenv (or pyenv, venv...)
- Cookiecutter (to install the template)

## How to install

 1. Install cookiecutter. Instructions [here](https://cookiecutter.readthedocs.io/en/1.7.2/installation.html)
 2. Run `cookiecutter https://github.com/dymmond/esmerald-scaffold` and follow the instructions.
 3. `make requirements` - Installs all the requirements needed for dev and testing.
 4. `make` to list all the available commands for the project.

## Run locally

- `make run` or if you wish to run with a different set of settings:
    1. `ESMERALD_SETTINGS_MODULE=name_of_module.file.class_name python -m {{ cookiecutter.project_src_name }}.serve`

- You should be able to access `http://127.0.0.1:8001/` and test the endpoints.

## Settings

The project comes with pre-set of configurations located at
`{{ cookiecutter.project_root_name }}/{{ cookiecutter.project_src_name }}/core/configs/`.

## Run tests

- `make test` - Runs all the standard tests.

## OpenAPI

To access the documentation of the project.

1. `make run` - Starts the project,
2. `http://localhost:8001/docs/swagger` to access the swagger docs.
2. `http://localhost:8001/docs/redoc` to access the redoc docs.
