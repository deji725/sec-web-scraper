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


# check if directory index_sec exists
def test_build_sec_pass():
    # integ test
    d = Downloader()
    res = d.build_index_sec(2000, 2002)
    assert os.path.exists('./index_sec/')


@patch('builtins.print')
def test_build_sec_fail(mock_print):
    d = Downloader()
    res = d.build_index_sec(2010, 2011)
    assert mock_print.call_args.args == ('trying to do Latin encoding',)


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
