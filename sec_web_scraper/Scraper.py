"""Scraping functions."""

import re

# import time
# import unicodedata as unc
# import urllib
# Stopwords dictionary
# import nltk
# nltk.download('punkt')
import json

# options.headless = True
# geckodriver = '/user/oko2107/Downloads/geckodriver'
# driver =  webdriver.Firefox(service=Service(geckodriver))
# import os


# import numpy as np
import pandas as pd
import requests

# import io
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# chrome_options = Options()
# chrome_options.add_argument("--headless=new")
# service = Service(ChromeDriverManager().install())

# driver = webdriver.Chrome(service=service,options=chrome_options)

# from pandas.core.frame import DataFrame
# from tqdm import trange

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox",
    "Accept": "application/json, text/javascript, */*; q=0.01",
}
sample_10k = "https://www.sec.gov/Archives/edgar/data/20/0000893220-96-000500.txt"


def create_selenium_browser_headless(
    sec_link: str = 'https://www.sec.gov/edgar/search/',
) -> webdriver.chrome.webdriver.WebDriver:
    """Creates a Selenium Headless Web Browser for Full Text Search.

    The goal of this method is to perform full text search queries by using SEC EDGAR's full text page.
    There used to be a public API for this but it has been removed.

    Args:
        sec_link: The initial link for the Selenium Web Browser

    Returns:
        None

    Raises:
        ConnectionError: requests couldn\'t get your link so Selenium browser not created
    """
    r = requests.get(sec_link, headers)
    if r.ok:
        print("Good")
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        service = Service(ChromeDriverManager().install())

        driver = webdriver.Chrome(service=service, options=chrome_options)
        # driver = webdriver.Chrome(service=service)
        return driver
    else:
        raise ConnectionError('requests couldn\'t get your link so Selenium browser not created')
    # pass  # This will be for full text scraping


def get_filings_by_query(query: str, driver) -> pd.DataFrame:
    """Find the first 100 submissions that contain the specific query
     This method will look at the SEC EDGARs official database and perform a full-text-search on the provided query.
     #WARNING: sometimes it may return an empty DataFrame

    Args:
        query:A string query/keyword that you are looking for.
        driver: A selenium web driver created by create_selenium_browser_headless.

    Returns:
        A pandas DataFrame containing the columns:
           ['File Type','CIK','Filename','Date Filed', 'Company Name','File Link']
        See [pandas.DataFrame][] to learn more about Pandas DataFrames

    Raises:
        An Exception if DataFrame can't be generated after 10 iterations of selenium get.

    """
    # service = Service(ChromeDriverManager().install())
    # chrome_options = Options()
    # chrome_options.add_argument("--headless=new")
    # driver = webdriver.Chrome(service=service,options=chrome_options)
    list_return = []
    found = False
    i = 0
    while found is False and i != 15:
        driver.get(f'https://www.sec.gov/edgar/search/#/q={query}')
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        # search = soup.find_all('tr')
        search = soup.find(id='hits')
        new_search = search.find_all('tr')[1:]
        link_ = 'https://www.sec.gov/Archives/edgar/data/'
        column_names = ['File Type', 'CIK', 'Filename', 'Date Filed', 'Company Name', 'File Link']
        for ele in new_search:
            ele_attr = ele.find_all("td")
            # File name :
            file_type = ele_attr[0].text
            submission_num = ele_attr[0].a['data-adsh'].replace('-', '')
            file_name = ele_attr[0].a['data-file-name']
            cik = ele_attr[4].text.split()[1]
            file_link = f'{link_}/{cik}/{submission_num}/{file_name}'
            company_name = ele_attr[3].text
            date_filed = ele_attr[1].text
            list_return.append([file_type, cik, file_name, date_filed, company_name, file_link])
            # keep only file_name, file_type, cik, file_link,name
        driver.implicitly_wait(5)
        found = len(list_return) != 0
        i += 1

    # if i == 10:
    #    raise Exception("Tried 10 times, could not generate DataFrame")
    return pd.DataFrame(list_return, columns=column_names)


def get_company_filings_given_cik(cik: str) -> dict:
    """Find a company submission history given CIK.

     This method will look at the SEC EDGARs official submission history for a company
     based on the provided CIK.It will then get the JSON document containing this information.

    Args:
        cik: A 10 digit unique string representing each public company.Can be retrieved using Downloader
            get_company_info.

    Returns:
        A dict representing all the submission history for a partiular company (cik).
        The dict contains keys such as entityType,tickers,exchanges,stateofIncoporation,addresses, etc

        Empty dict is returned in the case that the CIK is invalid.
    Raises:
        AssertionError: Length of CIKs must be 10.

        Please see this link for more information: https://data.sec.gov/submissions/CIK0000320193.json
    """
    assert len(cik) == 10
    link = f"https://data.sec.gov/submissions/CIK{cik}.json"
    r = requests.get(link, headers=headers)
    if r.ok:
        company_filling_cik = json.loads(r.text)
        print(company_filling_cik["sicDescription"])

        return company_filling_cik
    else:
        return {}


def get_document_given_link(link: str) -> str:
    """Retrieve a document given it's URL

    Get the raw text of a document provided its URL

    Args:
        link: A url string for .txt file found on a documents's index page.
            For example, https://www.sec.gov/Archives/edgar/data/20/0000893220-96-000500.txt that can be retrieved
            from the index page: https://www.sec.gov/Archives/edgar/data/20/0000893220-96-000500-index.html
    Returns:
        None if document doesn't exist or a text str contaning the text
    """

    print(link)
    print(headers)
    r = requests.get(link, headers=headers)
    if r.ok:
        print("ok")
        return r.text
    else:
        return None


def get_document_tags(txt: str) -> list[tuple]:
    """Find all document tags inside of a document.

    The document tags in a document are very helfpul for identifying change of sections
    in a document.
    Args:
        txt: An HTML txt file (the output of get_document_given_link)

    Returns:
        A list of tuples of the form : (start_tag_index,end_tag_index,tag_name).
        One example: (1385 , 176135 , <TYPE>10-K) means the 10-K section start at index 1385 and
        ended at 176135.
    """
    try:
        doc_start = re.compile(r"<DOCUMENT>")
        doc_end = re.compile(r"</DOCUMENT>")
        doc_type = re.compile(r"<TYPE>[^\n]+")

        beg_seq = []
        for y in doc_start.finditer(txt):
            beg_seq.append(y.end())
        end_seq = []
        for y in doc_end.finditer(txt):
            end_seq.append(y.start())

        type_list = []
        for y in doc_type.findall(txt):
            type_list.append(y)

        results = []
        for (
            x,
            y,
            z,
        ) in zip(beg_seq, end_seq, type_list):
            results.append((x, y, z))
            print(f'This is x, y, z: {x} , {y} , {z}')
        return results
    except TypeError as t:
        print(f'Error : {t}')
        return None


def bs4_scraping_text(string_inp: str) -> BeautifulSoup:
    """A BeautifulSoup wrapper function for processing the text document we retrieved
    to utilize the lxml parser.

    Work in Progress.

    Args:
        string_inp: An HTML txt file (the output of get_document_given_link)

    Returns:
        A BeautifulSoup object
    """

    text = BeautifulSoup(string_inp, "lxml")
    return text
    # Wait until you process this. We want to get the text between two tags


def iterate_over_filings(filings: dict) -> int:
    """Extract number of filings for a company.

    This function will iterate over the filings dictionary and try to extract
    relevant information for the user. As of now, it only returns the total count
    of filings.

    Args:
        filings: A dictionary retrieved from get_company_filings_given_cik.
            get_company_filings_given_cik will return a nested dictionary.
            One can pass in the "filings" key of the dictionary returned by get_company_filings_given_cik.

    Returns:
        A count of all the filings recorded for this company
    """
    print(filings.keys())
    for k, v in filings["recent"].items():
        print(f"This is the key {k} and the item length: {len(v)} and type : {type(v)}")
    for j in filings["files"]:
        print(j)
        print(type(j))
    print("------")
    return filings["files"][0]["filingCount"]


class ScraperObject(object):
    """Work In Progress. Do Not Use

    A scraper that will parse sections and information from the retrieved files.

    Attributes:
        headers: Request headers to avoid bot detection for scraping
    """

    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox",
            "Accept": "application/json, text/javascript, */*; q=0.01",
        }

    # Implement methods to scrape from file
