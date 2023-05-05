# import re
# import json
import os
import pandas as pd
import requests
import io
import ast

# from bs4 import BeautifulSoup
from tqdm import trange


class Downloader(object):
    """This is a document downloader.

    Downloader will fetch documents from the EDGAR database based on parameters such as a
    text query, time period, company ticker, and file type.

    Attributes:
        forms: A set of all forms found from build_index_sec
        company_to_cik: A dictionary containing values (company_name,ticker,CIK)
        headers: Request headers to avoid bot detection for scraping
    """

    def __init__(self):
        """Initializes a Downloader object."""
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox",
            "Accept": "application/json, text/javascript, */*; q=0.01",
        }
        r = requests.get("https://www.sec.gov/files/company_tickers.json", headers=self.headers)
        self.company_to_cik = ast.literal_eval(r.text)
        self.forms = set()

    def build_index_sec(self, st: int, ed: int, path_files: str = './index_sec/') -> None:
        """Creates an index of SEC EDGAR filings based on range of years from [st,ed]

        Retrieves a list of filings starting from year st, quarter 1 to year ed, quarter 4.
        It will generate a tsv file for each (year,quarter) tuple that contains all the filings
        filed in that quarter and year.

        Args:
            st: starting year
            ed: ending year.
            path_files: file path for saving the built index

        Returns:
            None

        """
        # using this file from an open source project
        # https://github.com/pundrich/mate/pull/2/commits/b7e38c0f2684a4d8d598f16bb0724f7eb4d3f69c (using this PR)

        if os.path.exists(path_files) is False:
            os.makedirs(path_files)

        sec_url = "https://www.sec.gov/Archives/edgar/full-index/"
        column_names = ['CIK', 'Company Name', 'Form Type', 'Date Filed', 'Filename']
        dat_types = {"CIK": str, 'Company Name': str, 'Form Type': str, 'Date Filed': str, 'Filename': str}

        t_r = trange(st, ed + 1, desc='Downloading SEC files', leave=True)
        for year in t_r:
            for quarter in range(1, 5):
                t_r.set_description(f' Downloading SEC files for Year: {year} and QTR: {quarter} ')
                response = requests.get(sec_url + f"{year}/QTR{quarter}/master.zip", headers=self.headers)
                # print(response.ok)
                if response.ok:
                    try:
                        master_index = pd.read_csv(
                            io.BytesIO(response.content),
                            skiprows=11,
                            sep="|",
                            compression='zip',
                            names=column_names,
                            dtype=dat_types,
                        )
                    except Exception as e:
                        print(e)
                        print(f"{year}-QTR{quarter} failed")
                        print("trying to do Latin encoding")
                        master_index = pd.read_csv(
                            io.BytesIO(response.content),
                            skiprows=11,
                            sep="|",
                            compression='zip',
                            names=column_names,
                            dtype=dat_types,
                            encoding='latin-1',
                        )
                    master_index['url'] = master_index['Filename'].str.replace(".txt", '-index.html', regex=False)
                    master_index['CIK'] = master_index['CIK'].str.pad(10, side='left', fillchar='0')
                    save_file_path = os.path.join(path_files, f"{year}-QTR{quarter}.tsv")
                    master_index.to_csv(save_file_path, sep='|', index=False, header=False)
                    for i in master_index['Form Type']:
                        self.forms.add(i)
                else:
                    print(f'Error Code : {response.reason} for {year} and {quarter}')

    def read_tsv_files(self, path_files: str = './index_sec/') -> None:  # DON'T USE, Work in progress
        """Work in Progress."""
        # This should be called after build_index_sec
        list_dir_sec = os.listdir(path_files)
        if len(list_dir_sec) == 0:
            raise Exception(f"{path_files} is empty, this operation can't be run")
        # column_names = ['CIK', 'Company Name', 'Form Type', 'Date Filed', 'Filename']
        # dat_types = {"CIK": int, 'Company Name': str, 'Form Type': str, 'Date Filed': str, 'Filename': str}
        # for x in list_dir_sec
        # assert column_names != []
        # assert dat_types != []
        print("Nothing so far")

    def get_forms(self) -> list[str]:
        """Returns a list of all form types.

        This method will return a list of all form types found after the invocation of
        build_index_sec

        Returns:
            A list
            For example: ["10-K","10-Q"]
        """
        # A list of all forms reported within the period
        return list(self.forms)

    def pretty_print_forms(self) -> None:
        """Pretty Prints a list of all form types.

        This method will pretty print a list of all form types found after the invocation of
        build_index_sec

        """
        li_ = self.get_forms()
        for i in li_:
            print(f'Form Type : {i}')

    def get_company_info(self, company_name: str) -> list[tuple]:
        """Returns a list of possible company names.

        This method will return a list of possible company names given a query string company_name.
        It will find the top 10 matches based on the given string

        Args:
            company_name: A query string

        Returns:
            A list of tuples (CIK,ticker,title)
            For example:
            [(320193,'AAPL','Apple Inc'),(1418121,'APLE','Apple Hospitality REIT, Inc.')]
        """
        # Return the top 10 matches
        list_ret = []
        i = 0
        for k, v in self.company_to_cik.items():
            if company_name.lower() in v['title'].lower():
                list_ret.append(v)
                i += 1
            if i == 10:
                break
        return list_ret

    def find_files_by_type(self, form_type: str) -> pd.DataFrame:
        """Filters our index based on file type/form type.

        This method will filter our index based on the form_type provided to the function. Our index is
        a very large file and typically users will want to focus on a certain form type.

        Args:
            form_type: A form type found using get_forms()

        Returns:
            A pandas DataFrame containing the columns:
                ['CIK', 'Company Name', 'Form Type', 'Date Filed', 'Filename', 'url']
            Each entry in this DataFrame will contain 'Form Type' = form_type.
            See [pandas.DataFrame][] to learn more about Pandas DataFrames

        Raises:
            Exception: Form type does not exist

        """

        path_files = './index_sec/'
        column_names = ['CIK', 'Company Name', 'Form Type', 'Date Filed', 'Filename', 'url']
        dat_types = {"CIK": int, 'Company Name': str, 'Form Type': str, 'Date Filed': str, 'Filename': str}
        if form_type not in self.forms:
            raise Exception("form {form_type} does not exist")

        master_list = []
        for i in os.listdir(path_files):
            master_index = pd.read_csv(path_files + i, names=column_names, dtype=dat_types, sep='|')
            master_index = master_index[master_index['Form Type'] == form_type]
            master_list.append(master_index)
        return pd.concat(master_list)

    def find_files_by_company(self, company_cik: str) -> pd.DataFrame:
        """Filters our index based on company_cik in the given time period

        This method will filter our index based on the company_cik provided to the function. Our index is
        a very large file and typically users will want to focus on a certain company. Nicely formats the data
        for users in a DataFrame for easy extraction.

        Args:
            company_cik: A company's CIK. This can be found using get_company_info.

        Returns:
            A pandas DataFrame containing the columns:
                ['CIK', 'Company Name', 'Form Type', 'Date Filed', 'Filename', 'url']
            Each entry in this DataFrame will contain 'Company CIK' = company_cik.
            See [pandas.DataFrame][] to learn more about Pandas DataFrames

        Raises:
            Exception: Company CIK  does not exist

        """

        path_files = './index_sec/'
        column_names = ['CIK', 'Company Name', 'Form Type', 'Date Filed', 'Filename', 'url']
        dat_types = {"CIK": int, 'Company Name': str, 'Form Type': str, 'Date Filed': str, 'Filename': str}
        if len(company_cik) != 10:
            raise Exception("Company {company_cik} CIK is not 10 characters")

        master_list = []
        for i in os.listdir(path_files):
            master_index = pd.read_csv(path_files + i, names=column_names, dtype=dat_types, sep='|')
            master_index = master_index[master_index['CIK'] == company_cik]
            master_list.append(master_index)
        return pd.concat(master_list)
