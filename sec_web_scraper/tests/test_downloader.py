import pandas as pd
import pytest
import requests
import os
import io
import shutil  # for cleaning directory
from sec_web_scraper.Downloader import Downloader
from unittest.mock import patch, MagicMock

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox",
    "Accept": "application/json, text/javascript, */*; q=0.01",
}

indx_sec_path = './index_sec/'


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
    assert os.path.exists(indx_sec_path)


def test_get_forms_pass():
    assert len(d.get_forms()) != 0


def test_get_forms_mock():
    # Weak tests for now
    d = Downloader()
    d.get_forms = MagicMock(return_value=['10-K', '10-Q'])
    assert len(d.get_forms()) == 2


def test_read_tsv_files_empty_dir():  # DIRECTORy doens't exist
    d = Downloader()
    path = './empty_dir_sec'
    os.mkdir(path)
    with pytest.raises(Exception) as context:
        d.read_tsv_files(path)
    assert "this operation can't be run" in str(context.value)
    os.rmdir(path)
    # may change to sys.exit for a cleaner message


def test_read_tsv_files_DNE_dir():  # DIRECTORy doens't exist
    d = Downloader()
    with pytest.raises(FileNotFoundError) as context:
        d.read_tsv_files('./iindex_sec_fail')


@patch('builtins.print')
def test_read_tsv_files_pass(mock_print):
    d = Downloader()
    d.read_tsv_files(indx_sec_path)
    assert mock_print.call_args.args == ('Nothing so far',)


@patch('builtins.print')
def test_pretty_print_pass(mock_print):
    d.pretty_print_forms()
    assert 'Form Type' in mock_print.call_args.args[0]


def test_get_company_info_fail():
    assert d.get_company_info('x-y-z') == []


def test_get_company_info_pass():
    assert len(d.get_company_info('Apple')) != 0


def test_find_files_by_type_success():
    resp = d.find_files_by_type('8-K')
    assert resp.shape[0] > 0 and resp.shape[1] > 0


def test_find_files_by_type_fail():
    with pytest.raises(Exception) as context:
        d.find_files_by_type('XYZ-123')
    assert "does not exist" in str(context.value)


def test_find_files_by_company_empty():
    resp = d.find_files_by_company('0000104169')
    # We had a valid CIK but company did not exist in this range
    assert resp.shape[0] == 0


def test_find_files_by_company_fail_assert_fail():
    with pytest.raises(Exception) as context:
        # the provided CIK is not of length 10
        d.find_files_by_company('001104169')
    assert "10" in str(context.value)


# Last test
def test_cleanup_dir():
    shutil.rmtree(indx_sec_path)
    with pytest.raises(FileNotFoundError) as context:
        os.listdir(indx_sec_path)
