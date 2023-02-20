import requests
import urllib
import re
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import unicodedata as unc

# Stopwords dictionary
# import nltk
# nltk.download('punkt')
import json
from pandas.core.frame import DataFrame


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox",
    "Accept": "application/json, text/javascript, */*; q=0.01",
}
sample_10k = "https://www.sec.gov/Archives/edgar/data/20/0000893220-96-000500.txt"


def create_selenium_browser_headless():
    pass  # This will be for full text scraping


def get_company_filings_given_cik(cik):
    assert len(cik) == 10
    link = f"https://data.sec.gov/submissions/CIK{cik}.json"
    r = requests.get(link, headers=headers)
    company_filling_cik = json.loads(r.text)
    print(company_filling_cik["sicDescription"])

    return company_filling_cik


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

    print(type_list)


def bs4_scraping_text(string_inp):
    text = BeautifulSoup(string_inp, "lxml")
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


class Scraper(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox",
            "Accept": "application/json, text/javascript, */*; q=0.01",
        }


def main():
    sample_10k = "https://www.sec.gov/Archives/edgar/data/20/0000893220-96-000500.txt"
    raw_txt = get_document_given_link(sample_10k)
    doc_tags = get_document_tags(raw_txt)

    # Add checking to see if length of cik is 10 digits
    apple_cik = get_company_filings_given_cik("0000320193")
    print(f"These are the keys in the official SEC API based on CIK")
    print(apple_cik.keys())

    print(f"Iterating over the filings....")
    n = iterate_over_filings(apple_cik["filings"])
    print(f"This is the file count {n}")


if __name__ == "__main__":
    main()
