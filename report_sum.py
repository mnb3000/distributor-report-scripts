import pandas as pd
import argparse

argParser = argparse.ArgumentParser()
argParser.add_argument('-f', '--file', help='csv file path', required=True)
argParser.add_argument(
    '-ac',
    '--artist-column',
    help='artist column name (default "Artist")',
    default='Artist', dest='artist'
)
argParser.add_argument(
    '-rc',
    '--revenue-column',
    help='revenue column name (default "Net Revenue in USD")',
    default='Net Revenue in USD', dest='revenue'
)
argParser.add_argument(
    '-e',
    '--encoding',
    help='csv file encoding (default "utf8, but bandcamp needs "utf-16")',
    default='utf8',
)
args = argParser.parse_args()

dataFileName = args.file
artistColumn = args.artist
netRevenueColumn = args.revenue
encoding = args.encoding

df = pd.read_csv(dataFileName, encoding=encoding)

sums = df.groupby(artistColumn).agg({netRevenueColumn: 'sum'})
print(sums)
