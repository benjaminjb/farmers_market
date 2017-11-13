import unittest
from src.products import products

class TestingCase(unittest.TestCase):

    def test_product_specifications_chai(self):
        chai = products["chai"]
        expected_code = "CH1"
        expected_price = "3.11"
        self.assertEqual(chai["code"], expected_code, "Actual '{}' != expected '{}'".format(chai["code"], expected_code))
        self.assertEqual(chai["price"], expected_price, "Actual '{}' != expected '{}'".format(chai["price"], expected_price))

    def test_product_specifications_apples(self):
        apples = products["apples"]
        expected_code = "AP1"
        expected_price = "6.00"
        self.assertEqual(apples["code"], expected_code, "Actual '{}' != expected '{}'".format(apples["code"], expected_code))
        self.assertEqual(apples["price"], expected_price, "Actual '{}' != expected '{}'".format(apples["price"], expected_price))

    def test_product_specifications_coffee(self):
        # test_basket = basket_module.Basket()
        coffee = products["coffee"]
        expected_code = "CF1"
        expected_price = "11.23"
        self.assertEqual(coffee["code"], expected_code, "Actual '{}' != expected '{}'".format(coffee["code"], expected_code))
        self.assertEqual(coffee["price"], expected_price, "Actual '{}' != expected '{}'".format(coffee["price"], expected_price))

    def test_product_specifications_milk(self):
        milk = products["milk"]
        expected_code = "MK1"
        expected_price = "4.75"
        self.assertEqual(milk["code"], expected_code, "Actual '{}' != expected '{}'".format(milk["code"], expected_code))
        self.assertEqual(milk["price"], expected_price, "Actual '{}' != expected '{}'".format(milk["price"], expected_price))

    def test_product_specifications_oatmeal(self):
        oatmeal = products["oatmeal"]
        expected_code = "OM1"
        expected_price = "3.69"
        self.assertEqual(oatmeal["code"], expected_code, "Actual '{}' != expected '{}'".format(oatmeal["code"], expected_code))
        self.assertEqual(oatmeal["price"], expected_price, "Actual '{}' != expected '{}'".format(oatmeal["price"], expected_price))


if __name__ == "__main__":
    unittest.main()
