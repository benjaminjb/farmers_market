import unittest
from src.basket import Basket

class TestingCase(unittest.TestCase):

    def test_basket_order(self):
        test_basket = Basket()
        test_basket.add(("AP1", "6.00"))
        test_basket.add(("CF1", "11.23"))
        test_basket.add(("AP1", "6.00"))
        actual = test_basket.items_in_order()
        expected = [("AP1", "6.00"), ("CF1", "11.23"), ("AP1", "6.00")]
        self.assertEqual(actual, expected, "Actual '{}' != expected '{}'".format(actual, expected))

    def test_basket_counting(self):
        test_basket = Basket()
        test_basket.add(("AP1", "6.00"))
        test_basket.add(("CF1", "11.23"))
        test_basket.add(("AP1", "6.00"))
        actual = test_basket.items_in_total()
        expected = {("AP1", "6.00"): 2, ("CF1", "11.23"): 1}
        self.assertEqual(actual, expected, "Actual '{}' != expected '{}'".format(actual, expected))


if __name__ == "__main__":
    unittest.main()
