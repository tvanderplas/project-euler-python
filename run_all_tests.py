import os
import unittest

loader = unittest.TestLoader()
runner = unittest.TextTestRunner()

start_dir = os.getcwd() + '\\Tests'
suite = loader.discover(start_dir, pattern='*test.py')

runner.run(suite)
