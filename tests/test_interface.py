import unittest
from src.interface import *
import StringIO
import sys

class TestingCase(unittest.TestCase):

    def test_run_commands(self):
        capturedOutput = StringIO.StringIO()
        sys.stdout = capturedOutput
        run_commands("fail", {})
        actual = capturedOutput.getvalue()
        expected = '''
Please enter a recognized command:
    "add ____" to add an item to your basket,
    "sum" to see the current state of your basket,
    "clear" to start a new basket, or
    "checkout" to quit.
'''
        self.assertEqual(actual, expected, "Actual '{}' != expected '{}'".format(actual, expected))
        sys.stdout = sys.__stdout__


if __name__ == "__main__":
    unittest.main()
