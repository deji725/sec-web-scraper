from sec_web_scraper import *
from unittest.mock import patch
import pytest

test_link = "https://www.sec.gov/Archives/edgar/data/20/0000893220-96-000500.txt"
fail_link = "https://www.sec.gov/Archives/edgar/data/21/0000893220-96-000500.txt" #Should fail delibrately


def test_get_document_given_link_pass():
    assert get_document_given_link(test_link) is not None

def test_get_document_given_link_fail():
    assert get_document_given_link(fail_link) is None


def test_get_document_tags_pass():
    raw_text = get_document_given_link(test_link)
    assert get_document_tags(raw_text) is not None

def test_get_document_tags_exception():
    assert get_document_tags(None) is None
    #with pytest.raises(TypeError):
    #    get_document_tags(None)
        
#@patch('builtins.print')
#def test_print_hello(mock_print):
#    print_hello()
#    assert mock_print.call_args.args == ("Hello, world!",)
