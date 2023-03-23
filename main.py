from input import get_csv
from input import drop_duplicate
from input import drop_null
from input import datanonull
from input import capitalise_username
from test_main import test_duplicatesremoved
from test_main import test_nadropped
from test_main import test_capitalisedcolumns
import csv
import pytest
import pandas as pd
import numpy as np

def column(matrix, i):
    return [row[i] for row in matrix]

file = open('results.csv')
capitaliseddata = capitalise_username(file)
capitaliseddata = np.array(capitaliseddata)

print(capitaliseddata)
print(column(capitaliseddata,5))
print(capitaliseddata[5])

print(capitaliseddata)
print(capitaliseddata[1][5])
print(capitaliseddata[2][5])
capitaliseddata[1][5] == capitaliseddata[1][5].astype(int)
print(capitaliseddata[1][5])

b = [[i for i in item if i != ''] for item in capitaliseddata]

noblanks =[]
for i in capitaliseddata:
    if len([x for x in i if x != '']) == 6:
        noblanks.append(i)

noblanks = np.array(noblanks)
print(noblanks)

validated_answer3 = [x for x in noblanks[1:] if int(x[5]) > 0 and int(x[5])<11]
validated_answer3.insert(0, noblanks[0])
validated_answer3 = np.array(validated_answer3)
print(validated_answer3)

df = capitaliseddata
noblankentries = []
for row in capitaliseddata:
      if all(cell != '' for cell in row):
          noblankentries.append(row)

print(noblankentries)
noblankentries = pd.DataFrame(noblankentries)
print(noblankentries)
noblankentries.columns=noblankentries.iloc[0]
column_headers = list(noblankentries.columns.values)
print("The Column Header :", column_headers)
noblankentries = noblankentries.tail(-1)
print(noblankentries)
noblankentries = np.array(noblankentries)
isvalid_ans3 = [x for x in noblankentries[0:] if int(x[5]) == 1 or int(x[5]) == 2 or int(x[5]) == 3 or int(x[5]) == 4 or int(x[5]) == 5 or int(x[5]) == 6 or int(x[5]) == 7 or int(x[5]) == 8 or int(x[5]) == 9 or int(x[5]) == 10]
print(isvalid_ans3)
print(len(isvalid_ans3))
print(len(validated_answer3))





  

  


  
  









  
  
  


