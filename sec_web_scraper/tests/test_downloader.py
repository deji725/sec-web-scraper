import pandas as pd
import pytest
import requests
import os
import io
from sec_web_scraper.Downloader import Downloader
from unittest.mock import patch, MagicMock

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox",
    "Accept": "application/json, text/javascript, */*; q=0.01",
}


@patch('builtins.print')
def test_build_sec_fail(mock_print):
    d = Downloader()
    res = d.build_index_sec(2010, 2011)
    assert mock_print.call_args.args == ('trying to do Latin encoding',)


@patch('builtins.print')
def test_build_sec_index_invalid_link(mock_print):
    d = Downloader()
    d.headers = {}
    res = d.build_index_sec(2010, 2010)
    assert 'Error Code' in mock_print.call_args.args[0]


def test_2011_sec_full_index():
    # The 2011 Quarter 4 Test should fail
    sec_url = "https://www.sec.gov/Archives/edgar/full-index/"
    year = 2011
    quarter = 4
    column_names = ['CIK', 'Company Name', 'Form Type', 'Date Filed', 'Filename']
    dat_types = {"CIK": int, 'Company Name': str, 'Form Type': str, 'Date Filed': str, 'Filename': str}
    response = requests.get(sec_url + f"{year}/QTR{quarter}/master.zip", headers=headers)
    assert response.ok
    with pytest.raises(UnicodeDecodeError) as context:
        master_index = pd.read_csv(
            io.BytesIO(response.content),
            skiprows=11,
            sep="|",
            compression='zip',
            names=column_names,
            dtype=dat_types,
        )
    assert "invalid continuation byte" in str(context.value)


# check if directory index_sec exists

d = Downloader()
res = d.build_index_sec(2000, 2002)


def test_build_sec_pass():
    # integ test
    assert os.path.exists('./index_sec/')


def test_get_forms_pass():
    assert len(d.get_forms()) != 0


def test_get_forms_mock():
    # Weak tests for now
    d = Downloader()
    d.get_forms = MagicMock(return_value=['10-K', '10-Q'])
    assert len(d.get_forms()) == 2


def test_read_tsv_files_empty_dir():
    d = Downloader()
    with pytest.raises(FileNotFoundError) as context:
        d.read_tsv_files('./iindex_sec_fail')


@patch('builtins.print')
def test_read_tsv_files_pass(mock_print):
    d = Downloader()
    d.read_tsv_files('./index_sec/')
    assert mock_print.call_args.args == ('Nothing so far',)


#   @patch('builtins.print')
#   def test_pretty_print_pass(mock_print):
#
#       assert mock_print.call_args.args[0]
#
#   def test_pretty_print_mock():
#       d = Downloader()
#       d.pretty_print_forms = MagicMock(return_value=True)
#       assert d.pretty_print_forms() == True
