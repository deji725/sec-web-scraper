# sec-web-scraper
A Python based web scraper for the SEC EDGAR database

![Github](https://img.shields.io/github/license/deji725/sec-web-scraper)
![Issues](https://img.shields.io/github/issues/deji725/sec-web-scraper)
[![codecov](https://codecov.io/gh/deji725/sec-web-scraper/branch/main/graph/badge.svg?token=Y3RGEAR6Q2)](https://codecov.io/gh/deji725/sec-web-scraper)
![Github](https://github.com/deji725/sec-web-scraper/actions/workflows/makefile.yml/badge.svg)
## Overview

This library will for scraping certain financial documents from the EDGAR database such as the 10-K (and it's versions such as 10-K405,10-KSB), 20-F and 40-F. 

The two main features of the library will be:
- A document downloader portion that will fetch documents from the EDGAR database based on parameters such as a text query, time period, company ticker, and file type. 
- A scraper that will parse sections and information from the retrieved files. 

## Details
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

## References
- Python project template from https://github.com/ColumbiaOSS/example-project-python

