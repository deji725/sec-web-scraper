# import re
# import json
import os
import pandas as pd
import requests
import io

# from bs4 import BeautifulSoup
from tqdm import trange


class Downloader(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox",
            "Accept": "application/json, text/javascript, */*; q=0.01",
        }
        self.forms = set()

    def build_index_sec(self, st, ed, path_files='./index_sec'):
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
                    save_file_path = os.path.join(path_files, f"{year}-QTR{quarter}.tsv")
                    master_index.to_csv(save_file_path, sep='|', index=False, header=False)
                    for i in master_index['Form Type']:
                        self.forms.add(i)
                else:
                    print(f'Error Code : {response.reason} for {year} and {quarter}')

    def read_tsv_files(self, path_files='./index_sec'):
        # This should be called after build_index_sec
        list_dir_sec = os.listdir(path_files)
        if len(list_dir_sec) == 0:
            raise Exception(f"{path_files} is empty, this operation can't be run")
        # column_names = ['CIK', 'Company Name', 'Form Type', 'Date Filed', 'Filename']
        # dat_types = {"CIK": int, 'Company Name': str, 'Form Type': str, 'Date Filed': str, 'Filename': str}
        # assert column_names != []
        # assert dat_types != []
        print("Nothing so far")

    def get_forms(self):
        return list(self.forms)

    def pretty_print_forms(self):
        li_ = self.get_forms()
        for i in li_:
            print(f'Form Type : {i}')
