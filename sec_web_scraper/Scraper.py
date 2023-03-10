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
import os


# import numpy as np
import pandas as pd
import requests
import io
from bs4 import BeautifulSoup

# geckodriver for Firefox
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.ui import Select, WebDriverWait
# from webdriver_manager.firefox import GeckoDriverManager

# from webdriver_manager.chrome import ChromeDriverManager


# options = Options()

# from pandas.core.frame import DataFrame
from tqdm import trange

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox",
    "Accept": "application/json, text/javascript, */*; q=0.01",
}
sample_10k = "https://www.sec.gov/Archives/edgar/data/20/0000893220-96-000500.txt"


def create_selenium_browser_headless(sec_link='https://www.sec.gov/edgar/search/'):
    r = requests.get(sec_link, headers)
    if r.ok:
        print("Good")
        # driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
    else:
        raise ConnectionError('requests couldn\'t get your link so Selenium browser not created')
    # pass  # This will be for full text scraping


def get_company_filings_given_cik(cik):
    assert len(cik) == 10
    link = f"https://data.sec.gov/submissions/CIK{cik}.json"
    r = requests.get(link, headers=headers)
    if r.ok:
        company_filling_cik = json.loads(r.text)
        print(company_filling_cik["sicDescription"])

        return company_filling_cik
    else:
        return {}


def get_document_given_link(link):
    print(link)
    print(headers)
    r = requests.get(link, headers=headers)
    if r.ok:
        print("ok")
        return r.text
    else:
        return None


def get_document_tags(txt):
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


def bs4_scraping_text(string_inp):
    text = BeautifulSoup(string_inp, "lxml")
    return text
    # Wait until you process this. We want to get the text between two tags


def iterate_over_filings(filings):
    print(filings.keys())
    for k, v in filings["recent"].items():
        print(f"This is the key {k} and the item length: {len(v)} and type : {type(v)}")
    for j in filings["files"]:
        print(j)
        print(type(j))
    print("------")
    return filings["files"][0]["filingCount"]


def build_index_sec(st, ed, path_files='./index_sec'):
    # using this file from an open source project
    # https://github.com/pundrich/mate/pull/2/commits/b7e38c0f2684a4d8d598f16bb0724f7eb4d3f69c (using this PR)
    if os.path.exists(path_files) is False:
        os.makedirs(path_files)

    sec_url = "https://www.sec.gov/Archives/edgar/full-index/"
    column_names = ['CIK', 'Company Name', 'Form Type', 'Date Filed', 'Filename']
    dat_types = {"CIK": int, 'Company Name': str, 'Form Type': str, 'Date Filed': str, 'Filename': str}

    t_r = trange(st, ed + 1, desc='Downloading SEC files', leave=True)
    for year in t_r:
        for quarter in range(1, 5):
            t_r.set_description(f' Downloading SEC files for Year: {year} and QTR: {quarter} ')
            response = requests.get(sec_url + f"{year}/QTR{quarter}/master.zip", headers=headers)
            # print(response.ok)
            if response.ok:
                master_index = pd.read_csv(
                    io.BytesIO(response.content),
                    skiprows=11,
                    sep="|",
                    compression='zip',
                    names=column_names,
                    dtype=dat_types,
                )
                master_index['url'] = master_index['Filename'].str.replace(".txt", '-index.html', regex=False)
                save_file_path = os.path.join(path_files, f"{year}-QTR{quarter}.tsv")
                master_index.to_csv(save_file_path, sep='|', index=False, header=False)
            else:
                print(f'Error Code : {response.reason} for {year} and {quarter}')


class Scraper(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox",
            "Accept": "application/json, text/javascript, */*; q=0.01",
        }
