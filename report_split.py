import pandas as pd
import os
import argparse


argParser = argparse.ArgumentParser()
argParser.add_argument(
    '-p',
    '--prefix',
    help='prefix for generated reports (folder name and prefix in filename)',
    required=True
)
argParser.add_argument('-f', '--file', help='csv file path', required=True)
argParser.add_argument(
    '-ac',
    '--artist-column',
    help='artist column name (default "Artist")',
    default='Artist', dest='artist'
)
argParser.add_argument(
    '-e',
    '--encoding',
    help='csv file encoding (default "utf8, but bandcamp needs "utf-16")',
    default='utf8',
)
args = argParser.parse_args()

prefix = args.prefix
dataFileName = args.file
artistColumn = args.artist
encoding = args.encoding

df = pd.read_csv(dataFileName, encoding=encoding)

folderPath = os.path.join(os.path.curdir, prefix)
if not os.path.isdir(folderPath):
    print(f'Creating {folderPath} folder...')
    os.mkdir(folderPath)

print('Splitting up a report...')
artists = df[artistColumn].unique()
for artist in artists:
    print(f'Filtering for {artist}...')
    filename = f'{prefix}_{artist}.csv'
    filepath = os.path.join(folderPath, filename)
    filtered = df[df[artistColumn] == artist]
    filtered.to_csv(filepath)
    print(f'Saved {filename}')
