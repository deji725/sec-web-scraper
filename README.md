# sec-web-scraper
A Python based web scraper for the SEC EDGAR database

![Github](https://img.shields.io/github/license/deji725/sec-web-scraper)
![Issues](https://img.shields.io/github/issues/deji725/sec-web-scraper)

## Overview

This library will for scraping certain financial documents from the EDGAR database such as the 10-K (and it's versions such as 10-K405,10-KSB), 20-F and 40-F. 

The two main features of the library will be:
- A document downloader portion that will fetch documents from the EDGAR database based on parameters such as a text query, time period, company ticker, and file type. 
- A scraper that will parse sections and information from the retrieved files. 
