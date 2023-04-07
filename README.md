# sec-web-scraper
A Python based web scraper for the SEC EDGAR database

![Github](https://img.shields.io/github/license/deji725/sec-web-scraper)
![Issues](https://img.shields.io/github/issues/deji725/sec-web-scraper)
[![codecov](https://codecov.io/gh/deji725/sec-web-scraper/branch/main/graph/badge.svg?token=Y3RGEAR6Q2)](https://codecov.io/gh/deji725/sec-web-scraper)
![Github](https://github.com/deji725/sec-web-scraper/actions/workflows/makefile.yml/badge.svg)
[![docs](https://img.shields.io/github/actions/workflow/status/deji725/sec-web-scraper/docs.yml?label=docs)](https://deji725.github.io/sec-web-scraper/)
[![PyPI](https://img.shields.io/pypi/v/sec-web-scraper)](https://pypi.org/project/sec-web-scraper/)

## Overview

This library will for scraping certain financial documents from the EDGAR database such as the 10-K (and it's versions such as 10-K405,10-KSB), 20-F and 40-F. 

The two main features of the library will be:
- A document downloader portion that will fetch documents from the EDGAR database based on parameters such as a text query, time period, company ticker, and file type. 
- A scraper that will parse sections and information from the retrieved files. 

## Installation


Please make sure you have Python 3.7 or higher.

You can check your python version with

`python --version`

Then run the command below! 

`pip install sec-web-scraper`

## Usage

```py
# Downloader
from sec_web_scraper.Downloader import Downloader

# Create new downloader object
d = Downloader()

# input the year range for filing data
d.build_index_sec(2000, 2002)


# After you've built the index, see all forms type filed in that period as a list
d.get_forms()

# If you want to find the cik of company, provide the name (fuzzy match). Returns a list
d.get_company_info('apple')

# If you want all 8-K's filled in the range above.This is a DataFrame
res = d.find_files_by_type('8-K') 

#More features to be added!
``` 

```py
#Scraper
from sec_web_scraper.Scraper import *

#With a particular filing
sample_10k = "https://www.sec.gov/Archives/edgar/data/20/0000893220-96-000500.txt"

#Get the raw text
raw_txt = get_document_given_link(sample_10k)

#Get the sections in the document
doc_tags = get_document_tags(raw_txt)

#More features to be added!

```

## References
- Python project template from https://github.com/ColumbiaOSS/example-project-python

