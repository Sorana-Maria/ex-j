import requests
import numpy as np
import matplotlib.pylab as plt
import unittest
import pytest

from apicall import open_meteo
from plot import plot_data

def test_open_meteo_valid_input():
    # test with valid input (Berlin, Germany)
    data = open_meteo(52.52, 13.40)

    assert data is not None
    assert len(data['hourly']['temperature_2m']) == 24

def test_open_meteo_invalid_input():
    # test with invalid input (string instead of float)
    data = open_meteo("not a float", "not a float")

    assert data is None

def test_plot_data():
    # test with sample data
    sample_data = {'hourly': {'temperature_2m': [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14]}}

    # suppress the plot window from showing up
    #plt.show = lambda: None

    # calling the function should not raise any exceptions
    plot_data(sample_data)

pytest
'''
class TestMeteoAPI(unittest.TestCase):
    def test_open_meteo(self):
        # Test with valid inputs
        data = open_meteo(51.52, 5.48)
        self.assertIsNotNone(data)
        #self.assertTrue(isinstance(data, dict))

         # Test with invalid inputs
        data = open_meteo('51.5072', '-0.1276')  # string instead of float
        self.assertIsNone(data)
    def test_plot_data(self):
        # Test with valid data
        data = {'hourly': {'temperature_2m': [10, 12, 15, 16, 18, 21, 22, 20, 18, 16, 14, 12, 10, 10, 8, 7, 6, 6, 5, 4, 3, 3, 2, 2]}}
        plot_data(data)
        self.assertTrue(True) # We can't actually test if the plot is correct, so just make sure the function doesn't throw an error

        # Test with missing data
        data = {'wrong': 'data'}
        with self.assertRaises(AttributeError):
            plot_data(data)

if __name__ == "__main__":
    unittest.main()
'''
