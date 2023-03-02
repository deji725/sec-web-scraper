from sec_web_scraper import Scraper, get_document_given_link
from unittest.mock import patch

test_link = "https://www.sec.gov/Archives/edgar/data/20/0000893220-96-000500.txt"


def test_get_document_given_link():
    assert get_document_given_link(test_link) is not None


#   @patch('builtins.print')
#   def test_print_hello(mock_print):
#       print_hello()
#       assert mock_print.call_args.args == ("Hello, world!",)
