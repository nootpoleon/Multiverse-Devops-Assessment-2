from input import get_csv
from input import drop_duplicates

import pytest

data = get_csv('results.csv')
data = drop_duplicates('results.csv')

pytest.main()