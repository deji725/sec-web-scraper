# Contributing Guidelines


# How to develop on this project

`sec-web-scraper` welcomes contributions from the community.

## Setting up your own fork of this repo.

- On Github Repository Page, click on `Fork` button.
- Clone your fork of this repo. `git clone git@github.com:YOUR_GIT_USERNAME/sec-web-scraper.git`

## Install the project in develop mode

Run `make develop` to install and build this library and its dependencies using `pip`.

## Run the tests to ensure everything is working

Run `make test` to run the tests.

## Create a new branch to work on your contribution

Run `git checkout -b my_contribution`

## Make your changes

Edit the files using your preferred editor. (we recommend VIM or VSCode)

## Format the code

Run `make format` to format the code.

## Run the linter

Run `make lint` to run the linter.

## Test your changes

Please add test cases for your new changes!

Run `make test` to run the tests.
Run `make cov` to run the tests with coverage.

Ensure code coverage report shows `>90%` coverage, add tests to your PR.

## Commit your changes

Please make sure your commits messages are substantive.
I recommend squashing your commits before creating the pull request if they are not substantive.

## Push your changes to your fork

Run `git push origin my_contribution`

## Submit a pull request

On github interface, click on `Pull Request` button.

All Github CI Actions must pass before a merge will be allowed


## Make Details

This project is a pure python project using modern tooling. It uses a `Makefile` as a command registry, with the following commands:
- `make`: list available commands
- `make develop`: install and build this library and its dependencies using `pip`
- `make build`: build the library using `setuptools`
- `make lint`: perform static analysis of this library with `flake8` and `black`
- `make format`: autoformat this library using `black`
- `make annotate`: run type checking using `mypy`
- `make test`: run automated tests with `pytest`
- `make coverage`: run automated tests with `pytest` and collect coverage information
- `make dist`: package library for distribution


## Commands for generating documentation

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

