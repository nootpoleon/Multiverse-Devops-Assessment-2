import pytest
from input import *

file = open('results.csv')
data = get_csv(file)
data = drop_duplicate(data)
data = drop_null(data)
data = capitalise_username(data)
data = ans3valid(data)
data = exportcsv(data)
data = finalresult(data)