import pandas as pd
import os
import argparse

artistColumn = 'Artist'

argParser = argparse.ArgumentParser()
argParser.add_argument('-p', '--prefix', help='prefix for generated reports', required=True)
argParser.add_argument('-f', '--file', help='csv file path', required=True)
args = argParser.parse_args()

prefix = args.prefix
dataFileName = args.file

df = pd.read_csv(dataFileName)

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
