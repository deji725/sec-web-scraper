from unittest.mock import patch, MagicMock
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

import pandas as pd
import pytest
import requests
import os
from sec_web_scraper import *

test_link = "https://www.sec.gov/Archives/edgar/data/20/0000893220-96-000500.txt"
fail_link = "https://www.sec.gov/Archives/edgar/data/21/0000893220-96-000500.txt"  # Should fail delibrately

test_cik = "0000320193"


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox",
    "Accept": "application/json, text/javascript, */*; q=0.01",
}


def test_get_document_given_link_pass():
    assert get_document_given_link(test_link) is not None


def test_get_document_given_link_fail():
    assert get_document_given_link(fail_link) is None


def test_get_document_tags_pass():
    raw_text = get_document_given_link(test_link)
    assert get_document_tags(raw_text) is not None


def test_get_document_tags_exception():
    assert get_document_tags(None) is None


def test_get_company_filings_given_cik_pass():
    dict_comp = get_company_filings_given_cik(test_cik)
    assert bool(dict_comp)  # clever but empty dicts evalue to fale


def test_get_company_filings_given_cik_num_invalid_11_digits():
    # SHOULD SHOW AN ASSERTION ERROR
    # CIKs can only have 10 digits
    with pytest.raises(AssertionError) as asert_e:
        dict_comp = get_company_filings_given_cik(test_cik + '0')


def test_get_company_filings_given_cik_invalid_cik():
    # SHOULD SHOW AN ASSERTION ERROR
    # CIKs can only have 10 digits
    test_fake_cik = test_cik[:4] + '1' + test_cik[5:]
    print(test_fake_cik)
    dict_comp = get_company_filings_given_cik(test_fake_cik)
    assert not bool(dict_comp)  # clever but empty dicts evalue to fale


def test_iterate_over_filings_pass():
    # When you pass in an empty dict into iterate_over_filings
    apple_cik = get_company_filings_given_cik("0000320193")
    n = iterate_over_filings(apple_cik["filings"])
    assert n > 0


def test_iterate_over_filings_no_files():
    test_fake_cik = test_cik[:4] + '1' + test_cik[5:]
    print(test_fake_cik)
    dict_comp = get_company_filings_given_cik(test_fake_cik)

    with pytest.raises(KeyError) as asert_e:
        n = iterate_over_filings(dict_comp["filings"])


# Most likely this syntax for integration tests
@patch('builtins.print')
def test_create_selenium_browser_headless_pass(mock_print):
    create_selenium_browser_headless()
    assert mock_print.call_args.args == ("Good",)


def test_create_selenium_browser_headless_con_err():
    with pytest.raises(ConnectionError) as conn_er:
        create_selenium_browser_headless("https://www.sec.gov/edgar/2/2")
        print(f'{conn_er}')


def test_get_filings_by_query():
    service = Service(ChromeDriverManager().install())
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    test_data = get_filings_by_query('cookies', driver)
    assert test_data is not None


# @patch('Scraper.get_filings_by_query')
# def test_get_filings_by_query_failure():
