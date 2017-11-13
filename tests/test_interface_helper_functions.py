import unittest
from src.interface_helper_functions import *
import StringIO
import sys
from src.basket import Basket

class TestingCase(unittest.TestCase):

    def test_print_line(self):
        capturedOutput = StringIO.StringIO()
        sys.stdout = capturedOutput
        print_line(("AP1", "6.00"))
        print_line(("APOM", "-3.00"))
        actual = capturedOutput.getvalue()
        expected = '''AP1                            6.00
            APOM              -3.00
'''
        self.assertEqual(actual, expected, "Actual '{}' != expected '{}'".format(actual, expected))
        sys.stdout = sys.__stdout__

    def test_print_basket(self):
        capturedOutput = StringIO.StringIO()
        sys.stdout = capturedOutput
        test_basket = Basket()
        test_basket.add(("AP1", "6.00"))
        print_basket(test_basket)
        actual = capturedOutput.getvalue()
        expected = '''Item                          Price
----                          -----
AP1                            6.00
-----------------------------------
                               6.00
'''
        self.assertEqual(actual, expected, "Actual '{}' != expected '{}'".format(actual, expected))
        sys.stdout = sys.__stdout__

    def test_add_to_checkout_basket(self):
        capturedOutput = StringIO.StringIO()
        sys.stdout = capturedOutput
        test_basket = Basket()
        add_to_checkout_basket(test_basket, "apples")
        actual = test_basket.items_in_order()
        expected = [ ("AP1", "6.00") ]
        self.assertEqual(actual, expected, "Actual '{}' != expected '{}'".format(actual, expected))

        add_to_checkout_basket(test_basket, "apple")
        actual = capturedOutput.getvalue()
        expected = '''
Sorry, we don't recognize that product.
Please add one of the following:
    'coffee', 'chai', 'apples', 'oatmeal', 'milk'

'''
        self.assertEqual(actual, expected, "Actual '{}' != expected '{}'".format(actual, expected))
        sys.stdout = sys.__stdout__


if __name__ == "__main__":
    unittest.main()
