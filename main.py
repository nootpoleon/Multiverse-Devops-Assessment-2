import pytest
import csv
import pandas as pd
from input import ans3valid
from pathlib import Path

file = open('results.csv')

with open('cleansedresults.csv','w', newline='')as f:
  writer =csv.writer(f)
  writer.writerows(ans3valid(file))

path = Path('cleansedresults.csv')
print(path.is_file())

cleansedfile = open('cleansedresults.csv')
readcleansedfile = pd.read_csv(cleansedfile)
print(readcleansedfile)