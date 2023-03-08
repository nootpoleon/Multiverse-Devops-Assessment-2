from input import *

data = get_csv('results.csv')
print(data)

df = drop_duplicates('results.csv')
print(df)

df = drop_empty('results.csv')
print(df)