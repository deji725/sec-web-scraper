from Scraper import (
    get_company_filings_given_cik,
    iterate_over_filings,
    create_selenium_browser_headless,
    get_filings_by_query,
)
from Downloader import Downloader


def main():
    # sample_10k = "https://www.sec.gov/Archives/edgar/data/20/0000893220-96-000500.txt"
    # create_selenium_browser_headless()
    # build_index_sec(1993, 2000)
    # raw_txt = get_document_given_link(sample_10k)
    # doc_tags = get_document_tags(raw_txt)

    # print("These are the doc tags ")
    # print(doc_tags)
    # Add checking to see if length of cik is 10 digits
    apple_cik = get_company_filings_given_cik("0000320193")
    print("These are the keys in the official SEC API based on CIK")
    print(apple_cik.keys())

    print("Iterating over the filings....")
    n = iterate_over_filings(apple_cik["filings"])
    print(f"This is the file count {n}")
    # print(sample_10k)

    d = Downloader()
    d.build_index_sec(2010, 2010)  # Small Sample of Documents
    d.pretty_print_forms()
    d.read_tsv_files()
    driver = create_selenium_browser_headless()
    print(get_filings_by_query('cookies', driver))


if __name__ == "__main__":
    main()
