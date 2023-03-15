from input import get_csv
from input import drop_duplicate
from input import drop_null
from input import datanonull
from test_main import test_duplicatesremoved
from test_main import test_nadropped
import csv
import pytest
import pandas as pd
import numpy as np

file = open('results.csv')

def get_csv(file):
  file = open('results.csv')
  type(file)
  csvreader = csv.reader(file)
  data = list(csvreader)
  return data

data = get_csv('results.csv')

def drop_duplicate(file):
  no_duplicates = []
  for x in data:
    if x not in no_duplicates:
      no_duplicates.append(x)
  return no_duplicates

datanodupl = drop_duplicate(file)

def drop_null(file):
  remove_na = []
  for x in datanodupl:
    if x != ['','','','','','']:
      remove_na.append(x)
  return remove_na

datanonull = drop_null(file)

def column(matrix, i):
    return [row[i] for row in matrix]

def capitlise_username(file):
  capitalise = np.rec.fromrecords(datanonull, names = 'user_id, first_name, last_name, answer_1, answer_2, answer_3')
  capitalise['first_name'] = np.char.title(capitalise['first_name'])
  capitalise['last_name'] = np.char.title(capitalise['last_name'])
  capitalise[0] = 'user_id', 'first_name', 'last_name', 'answer_1', 'answer_2', 'answer_3'
  capitalise = capitalise.tolist()
  return capitalise
  
upperarr = capitlise_username(file)

print(upperarr)