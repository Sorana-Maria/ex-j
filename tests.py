import requests
import numpy as np
import matplotlib.pylab as plt
import unittest

from apicall import open_meteo
from plot import plot_data

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
