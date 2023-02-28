import pandas as pd
import argparse

artistColumn = 'Artist'
netRevenueColumn = 'Net Revenue in USD'

argParser = argparse.ArgumentParser()
argParser.add_argument('-f', '--file', help='csv file path', required=True)
args = argParser.parse_args()

dataFileName = args.file

df = pd.read_csv(dataFileName)

sums = df.groupby(artistColumn).agg({netRevenueColumn: 'sum'})
print(sums)
