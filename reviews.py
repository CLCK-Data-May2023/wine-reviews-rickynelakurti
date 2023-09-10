# add your code here
import pandas as pd

df = pd.read_csv('data/winemag-data-130k-v2.csv.zip', compression='zip', header=0, sep=',', quotechar='"')

summary = df.groupby('country').agg(count=('title', 'size'), points=('points', 'mean')).reset_index()

summary['points'] = summary['points'].round(1)

summary.to_csv('data/reviews-per-country.csv', index=False)

print("Summary saved to reviews-per-country.csv!")