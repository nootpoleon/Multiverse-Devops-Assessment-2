import pytest
import csv

from input import get_csv

def test_list():
  # Arrange
  file = open('results.csv')
  expected_result = list
  
  # Act
  output = type(get_csv(file))

  # Assert
  assert output == expected_result