"""
A Python based web scraper for the SEC EDGAR database.

This library will for scraping certain financial documents from the EDGAR database such as the 10-K
(and it's versions such as 10-K405,10-KSB), 20-F and 40-F.

The two main features of the library will be:

A document downloader portion that will fetch documents from the EDGAR database based on
parameters such as a text query, time period, company ticker, and file type.
A scraper that will parse sections and information from the retrieved files.

"""


from ._version import __version__
from sec_web_scraper.Downloader import Downloader
from sec_web_scraper.Scraper import *
