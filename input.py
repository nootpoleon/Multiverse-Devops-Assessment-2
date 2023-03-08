import csv
import pandas as pd
import numpy as np
from numpy import genfromtxt

def get_csv(file):
  global data
  file = open('results.csv')
  type(file)
  csvreader = csv.reader(file)
  data = list(csvreader)
  return data