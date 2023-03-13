import csv

def get_csv(file):
  file = open('results.csv')
  type(file)
  csvreader = csv.reader(file)
  data = list(csvreader)
  return data

data = get_csv('results.csv')

def drop_duplicates(file):
  no_duplicates = []
  for x in data:
    if x not in no_duplicates:
      no_duplicates.append(x)
  return no_duplicates
  