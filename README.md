# Distributor Report Scripts
These are my scripts for optimizing work process with music distribution companies, which provide big monthly/quarterly reports for your account. In case you are a label, like me, chances are that you have multiple artists distributed via your account, and you need to send them separate reports and figure out how much to pay them. These scripts are quite simple, but useful tools for exactly that.

**NEW:** Now there is an example below for usage with **Bandcamp** sales reports

## Requirements
You need `pandas` in order to use these scripts. You can install it via pip

```
$ pip install pandas
```

or use a distribution like `anaconda` and use the provided Jupyter notebook

## Usage

```
$ python3 report_split.py -h
usage: report_split.py [-h] -p PREFIX -f FILE

optional arguments:
  -h, --help            show this help message and exit
  -p PREFIX, --prefix PREFIX
                        prefix for generated reports (folder name and prefix in filename)
  -f FILE, --file FILE  csv file path
  -ac ARTIST, --artist-column ARTIST
                        artist column name (default "Artist")
  -e ENCODING, --encoding ENCODING
                        csv file encoding (default "utf8, but bandcamp needs "utf-16")
```

```
$ python3 report_sum.py -h
usage: report_sum.py [-h] -f FILE

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  csv file path
  -ac ARTIST, --artist-column ARTIST
                        artist column name (default "Artist")
  -rc REVENUE, --revenue-column REVENUE
                        revenue column name (default "Net Revenue in USD")
  -e ENCODING, --encoding ENCODING
                        csv file encoding (default "utf8, but bandcamp needs "utf-16")
```

## Customization/Examples
If you are not using the same distributor and/or report schema and your columns have different names - each script has those column names available as optional arguments, so you can easily customize it as it suits you

For **Bandcamp** the arguments would be:
```
$ python3 report_sum.py -ac artist -rc "net amount" -e utf-16 -f data.csv
```