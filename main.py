from input import *

data = get_csv('results.csv')
print(data)

data = drop_duplicates('results.csv')
print(data)