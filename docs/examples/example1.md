# SEC Web Scraper : Retrieving Financial Information

### Installation and Imports

We must first install the library and import the necessary functions from Downloader and Scraper 


```python
#Install the library
!pip install sec-web-scraper
#Output below:
```

    Requirement already satisfied: sec-web-scraper in /Users/deji/opt/miniconda3/lib/python3.9/site-packages (0.0.1)
    Requirement already satisfied: pandas in /Users/deji/opt/miniconda3/lib/python3.9/site-packages (from sec-web-scraper) (1.4.3)
    Requirement already satisfied: python-dateutil>=2.8.1 in /Users/deji/opt/miniconda3/lib/python3.9/site-packages (from pandas->sec-web-scraper) (2.8.2)
    Requirement already satisfied: numpy>=1.18.5 in /Users/deji/opt/miniconda3/lib/python3.9/site-packages (from pandas->sec-web-scraper) (1.23.1)
    Requirement already satisfied: pytz>=2020.1 in /Users/deji/opt/miniconda3/lib/python3.9/site-packages (from pandas->sec-web-scraper) (2022.1)
    Requirement already satisfied: six>=1.5 in /Users/deji/opt/miniconda3/lib/python3.9/site-packages (from python-dateutil>=2.8.1->pandas->sec-web-scraper) (1.16.0)



```python
#Import
from sec_web_scraper.Downloader import Downloader
from sec_web_scraper.Scraper import *
```

## Build the index for year range [2002,2006]

First, we want to create our downloader object. 

Since we haven't built the index, the forms attribute of our Downloader should be empty


```python
d = Downloader()
print(type(d))
#Output below:
```

    <class 'sec_web_scraper.Downloader.Downloader'>



```python
d.get_forms()
#Output below:
```




    []



Build the index using the `build_index_sec` function for our year range


```python
d.build_index_sec(2002,2006)
#Output below:
```

     Downloading SEC files for Year: 2006 and QTR: 4 : 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 5/5 [01:16<00:00, 15.23s/it]


Now, we can check the existence of forms and our newly created directory : `index_sec`


```python
len(d.get_forms())
#Output below:
```




    503



As we can see above, we have found 503 unique form types for this period (2002,2006).

Let's print some of them ,perhaps the first 10


```python
d.get_forms()[:10]
#Output below:
```




    ['5/A',
     '40-6B/A',
     'N-54A',
     'U-1',
     '40-8FC',
     '305B2/A',
     'F-4MEF',
     '19B-4E',
     '40-F',
     'NT 10-K']




```python
%ls index_sec/
#Output below:
```

    2002-QTR1.tsv  2003-QTR1.tsv  2004-QTR1.tsv  2005-QTR1.tsv  2006-QTR1.tsv
    2002-QTR2.tsv  2003-QTR2.tsv  2004-QTR2.tsv  2005-QTR2.tsv  2006-QTR2.tsv
    2002-QTR3.tsv  2003-QTR3.tsv  2004-QTR3.tsv  2005-QTR3.tsv  2006-QTR3.tsv
    2002-QTR4.tsv  2003-QTR4.tsv  2004-QTR4.tsv  2005-QTR4.tsv  2006-QTR4.tsv


As we can see above, we have generated indices for each (year,quarter) pair in our specified range

## Filter our index for forms of type 5/A

Now that we have our index, we can try to look for forms filed within year range with form type `5/A`.

The `find_files_by_type` function will do this for us!


```python
res = d.find_files_by_type('5/A')
res
#Output below:
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>CIK</th>
      <th>Company Name</th>
      <th>Form Type</th>
      <th>Date Filed</th>
      <th>Filename</th>
      <th>url</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>1000045</td>
      <td>NICHOLAS FINANCIAL INC</td>
      <td>5/A</td>
      <td>2006-01-25</td>
      <td>edgar/data/1000045/0000897069-06-000169.txt</td>
      <td>edgar/data/1000045/0000897069-06-000169-index....</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1000045</td>
      <td>NICHOLAS FINANCIAL INC</td>
      <td>5/A</td>
      <td>2006-01-25</td>
      <td>edgar/data/1000045/0000897069-06-000171.txt</td>
      <td>edgar/data/1000045/0000897069-06-000171-index....</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1000045</td>
      <td>NICHOLAS FINANCIAL INC</td>
      <td>5/A</td>
      <td>2006-01-25</td>
      <td>edgar/data/1000045/0000897069-06-000173.txt</td>
      <td>edgar/data/1000045/0000897069-06-000173-index....</td>
    </tr>
    <tr>
      <th>3987</th>
      <td>1006057</td>
      <td>NOVICH NEIL S</td>
      <td>5/A</td>
      <td>2006-01-06</td>
      <td>edgar/data/1006057/0000790528-06-000018.txt</td>
      <td>edgar/data/1006057/0000790528-06-000018-index....</td>
    </tr>
    <tr>
      <th>4820</th>
      <td>1008051</td>
      <td>MANN ALFRED E</td>
      <td>5/A</td>
      <td>2006-02-24</td>
      <td>edgar/data/1008051/0001209191-06-013293.txt</td>
      <td>edgar/data/1008051/0001209191-06-013293-index....</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>94781</th>
      <td>847431</td>
      <td>NYMAGIC INC</td>
      <td>5/A</td>
      <td>2002-10-18</td>
      <td>edgar/data/847431/0000902561-02-000488.txt</td>
      <td>edgar/data/847431/0000902561-02-000488-index.html</td>
    </tr>
    <tr>
      <th>105650</th>
      <td>898173</td>
      <td>O REILLY AUTOMOTIVE INC</td>
      <td>5/A</td>
      <td>2002-11-15</td>
      <td>edgar/data/898173/0000898173-02-000059.txt</td>
      <td>edgar/data/898173/0000898173-02-000059-index.html</td>
    </tr>
    <tr>
      <th>112364</th>
      <td>924717</td>
      <td>SURMODICS INC</td>
      <td>5/A</td>
      <td>2002-11-20</td>
      <td>edgar/data/924717/0000950134-02-014785.txt</td>
      <td>edgar/data/924717/0000950134-02-014785-index.html</td>
    </tr>
    <tr>
      <th>112365</th>
      <td>924717</td>
      <td>SURMODICS INC</td>
      <td>5/A</td>
      <td>2002-11-21</td>
      <td>edgar/data/924717/0000950134-02-014829.txt</td>
      <td>edgar/data/924717/0000950134-02-014829-index.html</td>
    </tr>
    <tr>
      <th>115707</th>
      <td>942011</td>
      <td>OREILLY LAWRENCE P</td>
      <td>5/A</td>
      <td>2002-11-15</td>
      <td>edgar/data/942011/0000898173-02-000059.txt</td>
      <td>edgar/data/942011/0000898173-02-000059-index.html</td>
    </tr>
  </tbody>
</table>
<p>3692 rows × 6 columns</p>
</div>



As we can see above, there are 3692 different 5/A filings!

## Scraper 

Now that we have our 5/A's, what if we wanted to scrape a particular company's filing? 

Let's choose Surmodics Inc (CIK : 0000924717) 5/A filed on 2002-11-20.

First, let's just look at the information available in the SEC database for Surmodics with `get_company_filings_given_cik`


```python
surmodics_dic = get_company_filings_given_cik('0000924717')
#Output below:
```

    Surgical & Medical Instruments & Apparatus



```python
surmodics_dic['addresses']
#Output below:
```




    {'mailing': {'street1': '9924 WEST 74TH ST',
      'street2': None,
      'city': 'EDEN PRAIRIE',
      'stateOrCountry': 'MN',
      'zipCode': '55344',
      'stateOrCountryDescription': 'MN'},
     'business': {'street1': '9924 W 74TH ST',
      'street2': None,
      'city': 'EDEN PRAIRIE',
      'stateOrCountry': 'MN',
      'zipCode': '55344',
      'stateOrCountryDescription': 'MN'}}




```python
surmodics_dic['filings']['files']
#Output below:
```




    [{'name': 'CIK0000924717-submissions-001.json',
      'filingCount': 438,
      'filingFrom': '1997-12-24',
      'filingTo': '2008-11-18'}]



Now, let's get the raw 5/A text

We can use our `get_document_given_link` function


```python
surmodics_link = "https://www.sec.gov/Archives/edgar/data/924717/0000950134-02-014785.txt"
```


```python
raw_txt = get_document_given_link(surmodics_link)
#Output below:
```

    https://www.sec.gov/Archives/edgar/data/924717/0000950134-02-014785.txt
    {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox', 'Accept': 'application/json, text/javascript, */*; q=0.01'}
    ok



```python
raw_txt
#Output below:
```




    '-----BEGIN PRIVACY-ENHANCED MESSAGE-----\nProc-Type: 2001,MIC-CLEAR\nOriginator-Name: webmaster@www.sec.gov\nOriginator-Key-Asymmetric:\n MFgwCgYEVQgBAQICAf8DSgAwRwJAW2sNKK9AVtBzYZmr6aGjlWyK3XmZv3dTINen\n TWSM7vrzLADbmYQaionwg5sDW3P6oaM5D3tdezXMm7z1T+B+twIDAQAB\nMIC-Info: RSA-MD5,RSA,\n Cp7qAyzP95tJvCUP8ipPYpigzAcjUT+1kQNxu+OvEfyg8h11sDb0IReng+8t/M0r\n VANkRIow3cmOm0XhWvBMkQ==\n\n<SEC-DOCUMENT>0000950134-02-014785.txt : 20021120\n<SEC-HEADER>0000950134-02-014785.hdr.sgml : 20021120\n<ACCEPTANCE-DATETIME>20021120143444\nACCESSION NUMBER:\t\t0000950134-02-014785\nCONFORMED SUBMISSION TYPE:\t5/A\nPUBLIC DOCUMENT COUNT:\t\t1\nCONFORMED PERIOD OF REPORT:\t20020930\nFILED AS OF DATE:\t\t20021120\n\nSUBJECT COMPANY:\t\n\n\tCOMPANY DATA:\t\n\t\tCOMPANY CONFORMED NAME:\t\t\tSURMODICS INC\n\t\tCENTRAL INDEX KEY:\t\t\t0000924717\n\t\tSTANDARD INDUSTRIAL CLASSIFICATION:\tADHESIVES & SEALANTS [2891]\n\t\tIRS NUMBER:\t\t\t\t411356149\n\t\tSTATE OF INCORPORATION:\t\t\tMN\n\t\tFISCAL YEAR END:\t\t\t0930\n\n\tFILING VALUES:\n\t\tFORM TYPE:\t\t5/A\n\t\tSEC ACT:\t\t1934 Act\n\t\tSEC FILE NUMBER:\t000-23837\n\t\tFILM NUMBER:\t\t02834607\n\n\tBUSINESS ADDRESS:\t\n\t\tSTREET 1:\t\t9924 W 74TH ST\n\t\tCITY:\t\t\tEDEN PRAIRIE\n\t\tSTATE:\t\t\tMN\n\t\tZIP:\t\t\t55344\n\t\tBUSINESS PHONE:\t\t6128292700\n\n\tMAIL ADDRESS:\t\n\t\tSTREET 1:\t\t9924 WEST 74TH ST\n\t\tCITY:\t\t\tEDEN PRAIRIE\n\t\tSTATE:\t\t\tMN\n\t\tZIP:\t\t\t55344\n\n\tFORMER COMPANY:\t\n\t\tFORMER CONFORMED NAME:\tBSI CORP\n\t\tDATE OF NAME CHANGE:\t19970506\n\nREPORTING-OWNER:\t\n\n\tCOMPANY DATA:\t\n\t\tCOMPANY CONFORMED NAME:\t\t\tMESLOW JOHN A\n\t\tCENTRAL INDEX KEY:\t\t\t0001182832\n\t\tRELATIONSHIP:\t\t\t\tDIRECTOR\n\n\tFILING VALUES:\n\t\tFORM TYPE:\t\t5/A\n\n\tBUSINESS ADDRESS:\t\n\t\tSTREET 1:\t\tC/O SURMODIES INC\n\t\tSTREET 2:\t\t9924 WEST 74TH ST\n\t\tCITY:\t\t\tEDEN PRIRIE\n\t\tSTATE:\t\t\tMN\n\t\tZIP:\t\t\t55344\n\t\tBUSINESS PHONE:\t\t9528292700\n\n\tMAIL ADDRESS:\t\n\t\tSTREET 1:\t\tC/O SURMODIES INC\n\t\tSTREET 2:\t\t9924 WEST 74TH ST\n\t\tCITY:\t\t\tEDEN PRAIRIE\n\t\tSTATE:\t\t\tMN\n\t\tZIP:\t\t\t55344\n</SEC-HEADER>\n<DOCUMENT>\n<TYPE>5/A\n<SEQUENCE>1\n<FILENAME>c73128je5za.htm\n<DESCRIPTION>AMENDMENT NO. 1 TO FORM 5\n<TEXT>\n<HTML>\n<HEAD>\n<TITLE>Surmodics, Inc.</TITLE>\n</HEAD>\n<BODY bgcolor="#FFFFFF">\n<!-- PAGEBREAK -->\n<H5 align="left" style="page-break-before:always">&nbsp;</H5><P>\n<P>\n<TABLE align="right" width="160" border="1" cellspacing="0" cellpadding="1">\n<TR><TD align="center" nowrap><FONT size="2">OMB APPROVAL</FONT></TD></TR>\n<TR><TD nowrap><FONT size="2">OMB Number: 3235-0362</FONT></TD></TR>\n<TR><TD nowrap><FONT size="2">Expires: January 31, 2005</FONT></TD></TR>\n<TR><TD nowrap><FONT size="2">Estimated average burden<BR>\nhours per response...1.0</FONT></TD></TR></TABLE>\n\n<BR clear="right">\n<BR clear="right">\n\n<P align="center"><FONT size="4"><B>UNITED STATES<BR>\nSECURITIES AND EXCHANGE COMMISSION</B></FONT><BR>\n<FONT size="3"><B>Washington, DC 20549</B></FONT>\n\n<P align="center"><FONT size="5"><B>FORM 5</B></FONT>\n<P>\n<P align="center"><FONT size="4"><B>ANNUAL STATEMENT OF CHANGES IN BENEFICIAL\nOWNERSHIP</B></FONT>\n<P align="center"><FONT size="3"><B>Filed pursuant to Section 16(a) of the\nSecurities Exchange Act of 1934,<BR>\nSection 17(a) of the Public Utility Holding Company Act of 1935 or<BR>\nSection 30(h) of the Investment Company Act of 1940</B></FONT>\n<P>\n<TABLE border="0" cellspacing="0" cellpadding="4">\n\n<TR valign="top">\n<TD><FONT face="wingdings">&#111;</FONT></TD>\n<TD><FONT size="2">Check box if no longer<BR>\nsubject to Section&nbsp;16.<BR>\nForm&nbsp;4 or Form&nbsp;5<BR>\nobligations may continue.<BR>\nSee Instruction&nbsp;1(b).</FONT></TD>\n</TR>\n\n<TR valign="top">\n<TD><FONT face="wingdings">&#111;</FONT></TD>\n<TD><FONT size="2">Form 3 Holdings Reported</FONT></TD>\n</TR>\n\n<TR valign="top">\n<TD><FONT face="wingdings">&#111;</FONT></TD>\n<TD><FONT size="2">Form 4 Transactions Reported</FONT></TD>\n</TR>\n</TABLE>\n\n<TABLE border="0" cellspacing="0" cellpadding="4" width="100%">\n<TR>\n<TD colspan="13"><HR noshade></TD>\n</TR>\n<TR valign="top">\n<TD width="1%"><FONT size="2"><B>1.</B></FONT></TD>\n<TD width="25%" colspan="4" nowrap><FONT size="2"><B>Name and Address of\nReporting<BR> Person*</B></FONT></TD>\n<TD width="1%"><FONT size="2"><B>2.</B></FONT></TD>\n<TD width="20%" colspan="4" nowrap><FONT size="2"><B>Issuer Name and Ticker or\nTrading<BR> Symbol</B></FONT></TD>\n<TD width="1%"><FONT size="2"><B>3.</B></FONT></TD>\n<TD width="20%" nowrap colspan="2"><FONT size="2"><B>I.R.S. Identification\nNumber of Reporting<BR> Person, if an entity</B> <I>(Voluntary)</I></FONT></TD>\n</TR>\n\n<TR valign="bottom">\n<TD><FONT size="2">&nbsp;</FONT></TD>\n<TD colspan="4" rowspan="3" valign="middle"><FONT size="2">Meslow John\nA.</FONT><HR size="1" noshade><I>(Last) (First) (Middle)</I></TD>\n<TD><FONT size="2">&nbsp;</FONT></TD>\n<TD colspan="4" rowspan="2" valign="bottom"><FONT size="2">SurModics, Inc.\n(SRDX)</FONT><HR size="1" noshade></TD>\n<TD><FONT size="2">&nbsp;</FONT></TD>\n<TD colspan="2" rowspan="2"><FONT size="2"></FONT><HR size="1" noshade></TD>\n</TR>\n\n<TR valign="top">\n<TD><FONT size="2">&nbsp;</FONT></TD>\n<TD><FONT size="2">&nbsp;</FONT></TD>\n</TR>\n\n\n<TR valign="top">\n<TD><FONT size="2">&nbsp;</FONT></TD>\n<TD><FONT size="2">&nbsp;</FONT></TD>\n<TD><FONT size="2">&nbsp;</FONT></TD>\n<TD><FONT size="2">&nbsp;</FONT></TD>\n<TD><FONT size="2">&nbsp;</FONT></TD>\n<TD><FONT size="2">&nbsp;</FONT></TD>\n<TD><FONT size="2">&nbsp;</FONT></TD>\n<TD><FONT size="2">&nbsp;</FONT></TD>\n<TD><FONT size="2">&nbsp;</FONT></TD>\n</TR>\n\n<TR valign="top">\n<TD><FONT size="2">&nbsp;</FONT></TD>\n<TD colspan="4" rowspan="2" valign="bottom"><FONT size="2">1386 Knollwood\nLane<BR>\n</FONT><HR size="1" noshade></TD>\n<TD><FONT size="2"><B>4.</B></FONT></TD>\n<TD colspan="4"><FONT size="2"><B>Statement for Month&#47;Year</B></FONT></TD>\n<TD><FONT size="2"><B>5.</B></FONT></TD>\n<TD colspan="2"><FONT size="2"><B>If Amendment, Date of Original</B>\n<I>(Month&#47;Year)</I></FONT></TD>\n</TR>\n\n<TR valign="top">\n<TD><FONT size="2">&nbsp;</FONT></TD>\n<TD><FONT size="2">&nbsp;</FONT></TD>\n<TD colspan="4"><FONT size="2">&nbsp;</FONT><HR size="1" noshade></TD>\n<TD><FONT size="2">&nbsp;</FONT></TD>\n<TD colspan="2"><FONT size="2">September 2002</FONT><HR size="1" noshade></TD>\n</TR>\n\n<TR valign="top">\n<TD><FONT size="2">&nbsp;</FONT></TD>\n<TD colspan="4"><FONT size="2"><I>(Street)</I></FONT></TD>\n<TD><FONT size="2"><B>6.</B></FONT></TD>\n<TD colspan="4"><FONT size="2"><B>Relationship of Reporting Person(s)<BR>\nto Issuer</B> <I>(Check All Applicable)</I></FONT></TD>\n<TD><FONT size="2"><B>7.</B></FONT></TD>\n<TD colspan="2"><FONT size="2"><B>Individual or Joint&#47;Group\nReporting</B><BR>\n<I>(Check Applicable Line)</I></FONT></TD>\n</TR>\n\n<TR valign="top">\n<TD><FONT size="2">&nbsp;</FONT></TD>\n<TD colspan="4" rowspan="3" valign="bottom"><FONT size="2">Mendota Heights MN\n55118</FONT><HR size="1" noshade><FONT size="2"><I>\n(City)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n(State)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (Zip)</I></FONT></TD>\n<TD><FONT size="2">&nbsp;</FONT></TD>\n<TD nowrap><FONT face="wingdings">&#120;</FONT></TD>\n<TD nowrap><FONT size="2">&nbsp;Director</FONT></TD>\n<TD width="1%" nowrap><FONT face="wingdings">&#111;</FONT></TD>\n<TD nowrap><FONT size="2">&nbsp;10% Owner</FONT></TD>\n<TD><FONT size="2">&nbsp;</FONT></TD>\n<TD><FONT face="wingdings">&#120;</FONT></TD>\n<TD><FONT size="2">Form filed by One Reporting Person</FONT></TD>\n</TR>\n\n<TR valign="top">\n<TD><FONT size="2">&nbsp;</FONT></TD>\n<TD><FONT size="2">&nbsp;</FONT></TD>\n<TD width="1%" nowrap><FONT face="wingdings">&#111;</FONT></TD>\n<TD colspan="3" nowrap><FONT size="2">&nbsp;Officer <I>(give title\nbelow)</I></FONT></TD>\n<TD><FONT size="2">&nbsp;</FONT></TD>\n<TD><FONT face="wingdings">&#111;</FONT></TD>\n<TD rowspan="2"><FONT size="2">Form filed by More than One Reporting\nPerson</FONT></TD>\n</TR>\n\n<TR valign="top">\n<TD><FONT size="2">&nbsp;</FONT></TD>\n<TD><FONT size="2">&nbsp;</FONT></TD>\n<TD width="1%" nowrap><FONT face="wingdings">&#111;</FONT></TD>\n<TD nowrap colspan="3"><FONT size="2">&nbsp;Other <I>(specify\nbelow)</I></FONT></TD>\n<TD><FONT size="2">&nbsp;</FONT></TD>\n</TR>\n\n<TR valign="top">\n<TD><FONT size="2">&nbsp;</FONT></TD>\n<TD colspan="4"><FONT size="2">&nbsp;</FONT></TD>\n<TD><FONT size="2">&nbsp;</FONT></TD>\n<TD nowrap></TD>\n<TD colspan="3"><FONT size="2"></FONT><HR size="1" noshade></TD>\n<TD><FONT size="2">&nbsp;</FONT></TD>\n<TD>&nbsp;</TD>\n<TD><FONT size="2">&nbsp;</FONT></TD>\n</TR>\n\n<TR>\n<TD colspan="13"><HR noshade></TD>\n</TR>\n</TABLE>\n\n\n<TABLE border="0" width="100%">\n\n<TR>\n<TD align="right" valign="top" width="1%"><FONT size="2">*</FONT></TD>\n<TD width="2%"><FONT size="2">&nbsp;</FONT></TD>\n<TD width="97%"><FONT size="2">If the form is filed by more than one reporting\nperson, see instruction 4(b)(v).</FONT></TD>\n</TR>\n\n</TABLE>\n\n<!-- PAGEBREAK -->\n<P><HR noshade><P>\n<H5 align="left" style="page-break-before:always">&nbsp;</H5><P>\n\n<TABLE border="0" cellspacing="0" cellpadding="2" width="100%">\n<TR valign="bottom">\n<TD width="2%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="5%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="2%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="8%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="2%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="9%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="2%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="3%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="4%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="2%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="1%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="1%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="1%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="3%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="1%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="3%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="1%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="2%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="3%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="4%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="3%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="2%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="6%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="2%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="4%"><FONT size="1">&nbsp;</FONT></TD>\n</TR>\n<TR>\n<TD colspan="25"><HR noshade></TD>\n</TR>\n<TR>\n<TD align="center" colspan="25"><FONT size="2"><B>Table I &#151; Non-Derivative\nSecurities Acquired, Disposed of, or Beneficially Owned</B></FONT></TD>\n</TR>\n<TR>\n<TD colspan="25"><HR noshade></TD>\n</TR>\n<TR valign="top">\n<TD><FONT size="1"><B>1.</B></FONT></TD>\n<TD><FONT size="1"><B>Title of<BR>Security</B><BR><I>(Instr. 3)</I></FONT></TD>\n<TD><FONT size="1"><B>2.</B></FONT></TD>\n<TD nowrap><FONT\nsize="1"><B>Transaction<BR>Date</B><BR><I>(Month&#47;Day&#47;Year)</I></FONT></TD>\n<TD><FONT size="1"><B>2A.</B></FONT></TD>\n<TD nowrap><FONT size="1"><B>Deemed Execution<BR>Date, if\nany</B><BR><I>(Month&#47;Day&#47;Year)</I></FONT></TD>\n<TD><FONT size="1"><B>3.</B></FONT></TD>\n<TD colspan="2"><FONT size="1"><B>Transaction<BR>Code</B><BR><I>(Instr.\n8)</I></FONT></TD>\n<TD><FONT size="1"><B>4.</B></FONT></TD>\n<TD colspan="7" nowrap><FONT size="1"><B>Securities Acquired (A)<BR>or Disposed\nof (D)</B><BR><I>(Instr. 3, 4 and 5)</I></FONT></TD>\n<TD><FONT size="1"><B>5.</B></FONT></TD>\n<TD colspan="3" nowrap><FONT size="1"><B>Amount of Securities<BR>Beneficially\nOwned<BR>at the End of Issuer\'s<BR>Fiscal Year</B><BR><I>(Instr. 3 and\n4)</I></FONT></TD>\n<TD><FONT size="1"><B>6.</B></FONT></TD>\n<TD nowrap><FONT size="1"><B>Ownership<BR>Form:<BR>Direct (D) or<BR>Indirect\n(I)</B><BR><I>(Instr. 4)</I></FONT></TD>\n<TD><FONT size="1"><B>7.</B></FONT></TD>\n<TD nowrap><FONT size="1"><B>Nature\nof<BR>Indirect<BR>Beneficial<BR>Ownership</B><BR><I>(Instr. 4)</I></FONT></TD>\n</TR>\n<TR>\n<TD colspan="25"><HR noshade></TD>\n</TR>\n<TR valign="bottom">\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD colspan="3" align="center"><FONT size="1"><B>Amount</B></FONT></TD>\n<TD align="center"><FONT size="1"><B>(A)<BR>or<BR>(D)</B></FONT></TD>\n<TD align="center" colspan="3"><FONT size="1"><B>Price</B></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD colspan="3"><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n</TR>\n\n<TR>\n<TD colspan="25"><HR noshade></TD>\n</TR>\n\n<TR valign="bottom" bgcolor="#eeeeee">\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">Common Stock </FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD colspan="2"><FONT size="1"> </FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD align="right" nowrap><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1"> </FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD align="right" nowrap><FONT size="1"></FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="right"><FONT size="1">28,000*</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">D</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n</TR>\n\n<TR>\n<TD colspan="25"><HR noshade></TD>\n</TR>\n\n<TR valign="bottom">\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"> </FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD colspan="2"><FONT size="1"> </FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD align="right" nowrap><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1"></FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD align="right" nowrap><FONT size="1"></FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n</TR>\n\n<TR>\n<TD colspan="25"><HR noshade></TD>\n</TR>\n\n<TR valign="bottom" bgcolor="#eeeeee">\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"> </FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD colspan="2"><FONT size="1"> </FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD align="right" nowrap><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1"></FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD align="right" nowrap><FONT size="1"></FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n</TR>\n\n<TR>\n<TD colspan="25"><HR noshade></TD>\n</TR>\n\n<TR valign="bottom">\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"> </FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD colspan="2"><FONT size="1"> </FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD align="right" nowrap><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1"></FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD align="right" nowrap><FONT size="1"></FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n</TR>\n\n<TR>\n<TD colspan="25"><HR noshade></TD>\n</TR>\n\n<TR valign="bottom" bgcolor="#eeeeee">\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"> </FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD colspan="2"><FONT size="1"> </FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD align="right" nowrap><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1"></FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD align="right" nowrap><FONT size="1"></FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n</TR>\n\n<TR>\n<TD colspan="25"><HR noshade></TD>\n</TR>\n\n<TR valign="bottom">\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"> </FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD colspan="2"><FONT size="1"> </FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD align="right" nowrap><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1"></FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD align="right" nowrap><FONT size="1"></FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n</TR>\n\n<TR>\n<TD colspan="25"><HR noshade></TD>\n</TR>\n\n<TR valign="bottom" bgcolor="#eeeeee">\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"> </FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD colspan="2"><FONT size="1"> </FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD align="right" nowrap><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1"></FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD align="right" nowrap><FONT size="1"></FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n</TR>\n\n<TR>\n<TD colspan="25"><HR noshade></TD>\n</TR>\n\n<TR valign="bottom">\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"> </FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD colspan="2"><FONT size="1"> </FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD align="right" nowrap><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1"></FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD align="right" nowrap><FONT size="1"></FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n</TR>\n\n<TR>\n<TD colspan="25"><HR noshade></TD>\n</TR>\n\n<TR valign="bottom" bgcolor="#eeeeee">\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"> </FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD colspan="2"><FONT size="1"> </FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD align="right" nowrap><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1"></FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD align="right" nowrap><FONT size="1"></FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n</TR>\n\n<TR>\n<TD colspan="25"><HR noshade></TD>\n</TR>\n\n<TR valign="bottom">\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"> </FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD colspan="2"><FONT size="1"> </FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD align="right" nowrap><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1"></FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD align="right" nowrap><FONT size="1"></FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n</TR>\n<TR>\n<TD colspan="25"><HR noshade></TD>\n</TR>\n</TABLE>\n\n<P align="center"><FONT size="2">Page 2</FONT>\n\n<!-- PAGEBREAK -->\n<P><HR noshade><P>\n<H5 align="left" style="page-break-before:always">&nbsp;</H5><P>\n<TABLE border="0" cellspacing="0" cellpadding="2" width="100%">\n<TR>\n<TD colspan="16"><HR noshade></TD>\n</TR>\n<TR>\n<TD align="center" colspan="16"><FONT size="2"><B>Table II &#151; Derivative\nSecurities Acquired, Disposed of, or Beneficially Owned<BR>&nbsp;&nbsp;(e.g.,\nputs, calls, warrants, options, convertible securities)</B></FONT></TD>\n</TR>\n\n<TR>\n<TD colspan="16"><HR noshade></TD>\n</TR>\n\n\n<TR valign="top">\n<TD><FONT size="1"><B>1.</B></FONT></TD>\n<TD nowrap><FONT size="1"><B>Title of Derivative<BR>Security</B><BR><I>(Instr.\n3)</I></FONT></TD>\n<TD><FONT size="1"><B>2.</B></FONT></TD>\n<TD colspan="3" nowrap><FONT size="1"><B>Conversion or Exercise<BR>Price of\nDerivative<BR>Security</B></FONT></TD>\n<TD><FONT size="1"><B>3.</B></FONT></TD>\n<TD nowrap><FONT size="1"><B>Transaction\nDate</B><BR><I>(Month&#47;Day&#47;Year)</I></FONT></TD>\n<TD><FONT size="1"><B>3A.</B></FONT></TD>\n<TD nowrap><FONT size="1"><B>Deemed Execution<BR>Date, if\nany</B><BR><I>(Month&#47;Day&#47;Year)</I></FONT></TD>\n<TD><FONT size="1"><B>4.</B></FONT></TD>\n<TD colspan="2" nowrap><FONT size="1"><B>Transaction Code</B><BR><I>(Instr.\n8)</I></FONT></TD>\n<TD><FONT size="1"><B>5.</B></FONT></TD>\n<TD colspan="4" nowrap><FONT size="1"><B>Number of Derivative\nSecurities<BR>Acquired (A) or Disposed of (D)</B><BR><I>(Instr. 3, 4 and\n5)</I></FONT></TD>\n</TR>\n\n<TR>\n<TD colspan="16"><HR noshade></TD>\n</TR>\n\n\n<TR valign="bottom">\n<TD width="2%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="10%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="2%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="3%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="4%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="4%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="2%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="9%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="2%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="9%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="2%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="4%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="5%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="2%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="5%" align="center"><FONT size="1"><B>(A)</B></FONT></TD>\n<TD width="5%" align="center"><FONT size="1"><B>(D)</B></FONT></TD>\n</TR>\n\n<TR>\n<TD colspan="16"><HR noshade></TD>\n</TR>\n\n<TR valign="bottom" bgcolor="#eeeeee">\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">Director Stock Option (Right to Buy)</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="2">&nbsp;</FONT></TD>\n<TD align="right"><FONT size="1">$14.0625*</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1">Previously Reported</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD align="center"><FONT size="1">&nbsp;</FONT></TD>\n<TD colspan="2"><FONT size="1"> </FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n</TR>\n\n<TR>\n<TD colspan="16"><HR noshade></TD>\n</TR>\n\n<TR valign="bottom">\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">Director Stock Option (Right to Buy)</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="2">&nbsp;</FONT></TD>\n<TD align="right"><FONT size="1">$25.094*</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1">Previously Reported</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD align="center"><FONT size="1">&nbsp;</FONT></TD>\n<TD colspan="2"><FONT size="1"> </FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n</TR>\n\n<TR>\n<TD colspan="16"><HR noshade></TD>\n</TR>\n\n<TR valign="bottom" bgcolor="#eeeeee">\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">Director Stock Option (Right to Buy)</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="2">&nbsp;</FONT></TD>\n<TD align="right"><FONT size="1">$34.85</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1">11/21/01</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD align="center"><FONT size="1">&nbsp;</FONT></TD>\n<TD colspan="2"><FONT size="1">A </FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1">1,000</FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n</TR>\n\n<TR>\n<TD colspan="16"><HR noshade></TD>\n</TR>\n\n<TR valign="bottom">\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="2">&nbsp;</FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD align="center"><FONT size="1">&nbsp;</FONT></TD>\n<TD colspan="2"><FONT size="1"> </FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n</TR>\n\n<TR>\n<TD colspan="16"><HR noshade></TD>\n</TR>\n\n<TR valign="bottom" bgcolor="#eeeeee">\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="2">&nbsp;</FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD align="center"><FONT size="1">&nbsp;</FONT></TD>\n<TD colspan="2"><FONT size="1"> </FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n</TR>\n\n<TR>\n<TD colspan="16"><HR noshade></TD>\n</TR>\n\n<TR valign="bottom">\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="2">&nbsp;</FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD align="center"><FONT size="1">&nbsp;</FONT></TD>\n<TD colspan="2"><FONT size="1"> </FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n</TR>\n\n<TR>\n<TD colspan="16"><HR noshade></TD>\n</TR>\n\n<TR valign="bottom" bgcolor="#eeeeee">\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="2">&nbsp;</FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD align="center"><FONT size="1">&nbsp;</FONT></TD>\n<TD colspan="2"><FONT size="1"> </FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n</TR>\n\n<TR>\n<TD colspan="16"><HR noshade></TD>\n</TR>\n\n<TR valign="bottom">\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="2">&nbsp;</FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD align="center"><FONT size="1">&nbsp;</FONT></TD>\n<TD colspan="2"><FONT size="1"> </FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n</TR>\n\n<TR>\n<TD colspan="16"><HR noshade></TD>\n</TR>\n\n<TR valign="bottom" bgcolor="#eeeeee">\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="2">&nbsp;</FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD align="center"><FONT size="1">&nbsp;</FONT></TD>\n<TD colspan="2"><FONT size="1"> </FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n</TR>\n\n<TR>\n<TD colspan="16"><HR noshade></TD>\n</TR>\n\n<TR valign="bottom">\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="2">&nbsp;</FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD align="center"><FONT size="1">&nbsp;</FONT></TD>\n<TD colspan="2"><FONT size="1"> </FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n</TR>\n\n<TR>\n<TD colspan="16"><HR noshade></TD>\n</TR>\n\n</TABLE>\n\n\n<P align="center"><FONT size="2">Page 3</FONT>\n\n<!-- PAGEBREAK -->\n<P><HR noshade><P>\n<H5 align="left" style="page-break-before:always">&nbsp;</H5><P>\n\n<TABLE border="0" cellspacing="0" cellpadding="0" width="100%">\n<TR>\n<TD colspan="18"><HR noshade></TD>\n</TR>\n<TR>\n<TD align="center" colspan="18"><FONT size="2"><B>Table II &#151; Derivative\nSecurities Acquired, Disposed of, or Beneficially Owned &#151;\nContinued<BR>(e.g., puts, calls, warrants, options, convertible\nsecurities)</B></FONT></TD>\n</TR>\n<TR>\n<TD colspan="18"><HR noshade></TD>\n</TR>\n<TR valign="top">\n<TD><FONT size="1"><B>6.</B></FONT></TD>\n<TD colspan="2"><FONT size="1"><B>Date Exercisable and<BR>Expiration\nDate</B><BR><I>(Month&#47;Day&#47;Year)</I></FONT></TD>\n<TD><FONT size="1"><B>7.</B></FONT></TD>\n<TD colspan="2"><FONT size="1"><B>Title and Amount\nof<BR>Underlying Securities</B><BR><I>(Instr. 3 and 4)</I></FONT></TD>\n<TD><FONT size="1"><B>8.</B></FONT></TD>\n<TD colspan="3"><FONT size="1"><B>Price of\nDerivative<BR>Security</B><BR><I>(Instr. 5)</I></FONT></TD>\n<TD><FONT size="1"><B>9.</B></FONT></TD>\n<TD colspan="3" nowrap><FONT size="1"><B>Number of Derivative<BR>Securities\nBeneficially<BR>\nOwned at End of<BR>\nYear</B><BR><I>(Instr. 4)</I></FONT></TD>\n<TD><FONT size="1"><B>10.</B></FONT></TD>\n<TD nowrap><FONT size="1"><B>Ownership of <BR>Derivative Security:<BR>Direct\n(D)<BR>or Indirect (I)</B><BR><I>(Instr. 4)</I></FONT></TD>\n<TD><FONT size="1"><B>11.</B></FONT></TD>\n<TD nowrap><FONT size="1"><B>Nature\nof<BR>Indirect<BR>Beneficial<BR>Ownership</B><BR><I>(Instr. 4)</I></FONT></TD>\n</TR>\n\n<TR>\n<TD colspan="18" valign="top"><HR noshade></TD>\n</TR>\n\n<TR valign="bottom">\n<TD width="2%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="4%" align="center" nowrap><FONT\nsize="1"><B>Date<BR>Exercisable</B></FONT></TD>\n<TD width="4%" align="center" nowrap><FONT\nsize="1"><B>Expiration<BR>Date</B></FONT></TD>\n<TD width="2%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="4%"><FONT size="1"><B>Title</B></FONT></TD>\n<TD width="4%" align="center" nowrap><FONT size="1"><B>Amount or<BR>Number\nof<BR>Shares</B></FONT></TD>\n<TD width="2%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="1%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="3%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="2%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="2%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="2%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="4%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="2%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="2%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="8%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="2%"><FONT size="1">&nbsp;</FONT></TD>\n<TD width="5%"><FONT size="1">&nbsp;</FONT></TD>\n</TR>\n\n<TR>\n<TD colspan="18"><HR noshade></TD>\n</TR>\n\n<TR valign="bottom" bgcolor="#eeeeee">\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1">(1)</FONT></TD>\n<TD align="center"><FONT size="1">3/20/10</FONT></TD>\n<TD align="center"><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">Common Stock</FONT></TD>\n<TD align="right"><FONT size="1">10,000*</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD width="1%" align="right"><FONT size="2">&nbsp;</FONT></TD>\n<TD width="4%" align="right" nowrap><FONT size="1">None</FONT></TD> <TD><FONT\nsize="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="right"><FONT size="1">10,000*</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">D</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n</TR>\n\n<TR>\n<TD colspan="18"><HR noshade></TD>\n</TR>\n\n<TR valign="bottom">\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1">(2)</FONT></TD>\n<TD align="center"><FONT size="1">9/18/10</FONT></TD>\n<TD align="center"><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">Common Stock</FONT></TD>\n<TD align="right"><FONT size="1">2000*</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD width="1%" align="right"><FONT size="2">&nbsp;</FONT></TD>\n<TD width="4%" align="right" nowrap><FONT size="1">None</FONT></TD> <TD><FONT\nsize="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="right"><FONT size="1">2,000*</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">D</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n</TR>\n\n<TR>\n<TD colspan="18"><HR noshade></TD>\n</TR>\n\n<TR valign="bottom" bgcolor="#eeeeee">\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1">(3)</FONT></TD>\n<TD align="center"><FONT size="1">11/21/11</FONT></TD>\n<TD align="center"><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">Common Stock</FONT></TD>\n<TD align="right"><FONT size="1">1,000</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD width="1%" align="right"><FONT size="2">&nbsp;</FONT></TD>\n<TD width="4%" align="right" nowrap><FONT size="1">None</FONT></TD> <TD><FONT\nsize="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="right"><FONT size="1">1,000</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">D</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n</TR>\n\n<TR>\n<TD colspan="18"><HR noshade></TD>\n</TR>\n\n<TR valign="bottom">\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD width="1%" align="right"><FONT size="2">&nbsp;</FONT></TD>\n<TD width="4%" align="right" nowrap><FONT size="1"></FONT></TD> <TD><FONT\nsize="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n</TR>\n\n<TR>\n<TD colspan="18"><HR noshade></TD>\n</TR>\n\n<TR valign="bottom" bgcolor="#eeeeee">\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD width="1%" align="right"><FONT size="2">&nbsp;</FONT></TD>\n<TD width="4%" align="right" nowrap><FONT size="1"></FONT></TD> <TD><FONT\nsize="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n</TR>\n\n<TR>\n<TD colspan="18"><HR noshade></TD>\n</TR>\n\n<TR valign="bottom">\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD width="1%" align="right"><FONT size="2">&nbsp;</FONT></TD>\n<TD width="4%" align="right" nowrap><FONT size="1"></FONT></TD> <TD><FONT\nsize="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n</TR>\n\n<TR>\n<TD colspan="18"><HR noshade></TD>\n</TR>\n\n<TR valign="bottom" bgcolor="#eeeeee">\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD width="1%" align="right"><FONT size="2">&nbsp;</FONT></TD>\n<TD width="4%" align="right" nowrap><FONT size="1"></FONT></TD> <TD><FONT\nsize="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n</TR>\n\n<TR>\n<TD colspan="18"><HR noshade></TD>\n</TR>\n\n<TR valign="bottom">\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD width="1%" align="right"><FONT size="2">&nbsp;</FONT></TD>\n<TD width="4%" align="right" nowrap><FONT size="1"></FONT></TD> <TD><FONT\nsize="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n</TR>\n\n<TR>\n<TD colspan="18"><HR noshade></TD>\n</TR>\n\n<TR valign="bottom" bgcolor="#eeeeee">\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD width="1%" align="right"><FONT size="2">&nbsp;</FONT></TD>\n<TD width="4%" align="right" nowrap><FONT size="1"></FONT></TD> <TD><FONT\nsize="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n</TR>\n\n<TR>\n<TD colspan="18"><HR noshade></TD>\n</TR>\n\n<TR valign="bottom">\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1">&nbsp;</FONT></TD>\n<TD align="center"><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD width="1%" align="right"><FONT size="2">&nbsp;</FONT></TD>\n<TD width="4%" align="right" nowrap><FONT size="1"></FONT></TD> <TD><FONT\nsize="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD align="right"><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n<TD><FONT size="1">&nbsp;</FONT></TD>\n<TD><FONT size="1"></FONT></TD>\n</TR>\n\n<TR>\n<TD colspan="18"><HR noshade></TD>\n</TR>\n</TABLE>\n\n<P><FONT size="2"><B>Explanation of Responses:</B></FONT>\n<P>\n<P><FONT size="2">*Adjusted to reflect 2-for-1 stock split effective\n12/6/00</FONT> <P>\n<P><FONT size="2">(1) Exercisable in annual increments of 2,000 shares each,\ncommencing 3/20/00.</FONT> <P>\n<P><FONT size="2">(2) Exercisable in annual increments of 400 shares each,\ncommencing 9/18/00.</FONT> <P>\n<P><FONT size="2">(3) Exercisable in annual increments of 200 shares each,\ncommencing 11/21/01.</FONT> <P>\n<TABLE border="0" width="65%" align="center">\n<TR valign="bottom">\n<TD align="center" width="30%"><FONT size="2">/s/ John A. Meslow</FONT></TD>\n<TD width="5%"><FONT size="2">&nbsp;</FONT></TD>\n<TD align="center" width="30%"><FONT size="2">November 17, 2002</FONT></TD>\n</TR>\n\n<TR>\n<TD valign="top" align="center"><HR size="1" noshade><FONT size="2">**Signature\nof Reporting Person</FONT></TD>\n<TD><FONT size="2">&nbsp;</FONT></TD>\n<TD valign="top" align="center"><HR size="1" noshade><FONT\nsize="2">Date</FONT></TD>\n</TR>\n</TABLE>\n\n<P>\n<HR size="1" width="18%" noshade align="left">\n\n<TABLE border="0" width="100%">\n\n<TR>\n<TD align="right" valign="top" width="1%"><FONT size="2">**</FONT></TD>\n<TD width="2%"><FONT size="2">&nbsp;</FONT></TD>\n<TD width="97%"><FONT size="2">Intentional misstatements or omissions of facts\nconstitute Federal Criminal Violations. See 18&nbsp;U.S.C.&nbsp;1001 and\n15&nbsp;U.S.C.&nbsp;78ff(a).</FONT></TD>\n</TR>\n\n<TR>\n<TD colspan="3"><FONT size="2">&nbsp;</FONT></TD>\n</TR>\n\n<TR>\n<TD align="right" valign="top"><FONT size="2">Note:</FONT></TD>\n<TD><FONT size="2">&nbsp;</FONT></TD>\n<TD><FONT size="2">File three copies of this Form, one of which must be manually\nsigned. If space provided is insufficient, see Instruction 6 for\nprocedure.</FONT></TD>\n</TR>\n\n</TABLE>\n\n\n<P align="center"><FONT size="2">Page 4</FONT>\n\n</BODY>\n</HTML>\n\n</TEXT>\n</DOCUMENT>\n</SEC-DOCUMENT>\n-----END PRIVACY-ENHANCED MESSAGE-----\n'



Woah, that's a lot of text. Let's look for the tags in the document!


```python
get_document_tags(raw_txt)
#Output below:
```

    This is x, y, z: 1856 , 45504 , <TYPE>5/A





    [(1856, 45504, '<TYPE>5/A')]



As we see above, there is only 1 tag in this document for the 5/A. This means there is only 1 section in this document that starts from index 1856 and ends at index 45504
