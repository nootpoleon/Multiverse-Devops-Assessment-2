import pytest
import csv
from input import ans3valid

file = open('results.csv')

with open('cleansedresults.csv','w', newline='')as f:
  writer =csv.writer(f)
  writer.writerows(ans3valid(file))
