import unittest
from src.basket import Basket
from src.discount_calculator import *
from collections import defaultdict

class TestingCase(unittest.TestCase):

    def test_decide_discounts_coffee(self):
        bogo_deal = ("BOGO","-11.23","CF1")
        coffee_order = ("CF1", "11.23")

        test_basket = Basket()
        test_basket.add(coffee_order)
        coffee = test_basket.items_in_total()
        discount_list_none = decide_discounts(coffee)
        expected = defaultdict(int)
        self.assertDictEqual(discount_list_none, expected, "Actual '{}' != expected '{}'".format(discount_list_none, expected))

        test_basket.add(coffee_order)
        coffees = test_basket.items_in_total()
        discount_list_coffees = decide_discounts(coffees)
        expected = defaultdict(int)
        expected[bogo_deal] = 1
        self.assertDictEqual(discount_list_coffees, expected, "Actual '{}' != expected '{}'".format(discount_list_coffees, expected))

    def test_decide_discounts_apples(self):
        apple_deal = ("APPL","-1.50","AP1")
        apple_order = ("AP1", "6.00")
        coffee_order = ("CF1", "11.23")

        test_basket = Basket()
        test_basket.add(apple_order)
        test_basket.add(coffee_order)
        apples = test_basket.items_in_total()
        discount_list_none = decide_discounts(apples)
        expected = defaultdict(int)
        self.assertDictEqual(discount_list_none, expected, "Actual '{}' != expected '{}'".format(discount_list_none, expected))

        test_basket.add(apple_order)
        test_basket.add(apple_order)
        apples = test_basket.items_in_total()
        discount_list_apples = decide_discounts(apples)
        expected[apple_deal] = 3
        self.assertDictEqual(discount_list_apples, expected, "Actual '{}' != expected '{}'".format(discount_list_apples, expected))

    def test_decide_discounts_chai_milk(self):
        chai_milk_deal = ("CHMK","-4.75","MK1")
        apple_order = ("AP1", "6.00")
        chai_order = ("CH1", "3.11")
        milk_order = ("MK1", "4.75")

        test_basket = Basket()
        test_basket.add(chai_order)
        test_basket.add(apple_order)
        chai_milk = test_basket.items_in_total()
        discount_list_none = decide_discounts(chai_milk)
        expected = defaultdict(int)
        self.assertDictEqual(discount_list_none, expected, "Actual '{}' != expected '{}'".format(discount_list_none, expected))

        test_basket.add(milk_order)
        chai_milk = test_basket.items_in_total()
        discount_list_chai_milk = decide_discounts(chai_milk)
        expected[chai_milk_deal] = 1
        self.assertDictEqual(discount_list_chai_milk, expected, "Actual '{}' != expected '{}'".format(discount_list_chai_milk, expected))

        test_basket.add(chai_order)
        test_basket.add(milk_order)
        chai_milk = test_basket.items_in_total()
        discount_list_chai_milk_should_be_one = decide_discounts(chai_milk)
        self.assertDictEqual(discount_list_chai_milk_should_be_one, expected, "Actual '{}' != expected '{}'".format(discount_list_chai_milk_should_be_one, expected))

    def test_decide_discounts_apple_oatmeal(self):
        apple_oatmeal_deal = ("APOM","-3.00","AP1")
        apple_order = ("AP1", "6.00")
        chai_order = ("CH1", "3.11")
        oatmeal_order = ("OM1", "3.69")

        test_basket = Basket()
        test_basket.add(chai_order)
        test_basket.add(apple_order)
        apple_oatmeal = test_basket.items_in_total()
        discount_list_none = decide_discounts(apple_oatmeal)
        expected = defaultdict(int)
        self.assertDictEqual(discount_list_none, expected, "Actual '{}' != expected '{}'".format(discount_list_none, expected))

        test_basket.add(oatmeal_order)
        apple_oatmeal = test_basket.items_in_total()
        discount_list_apple_oatmeal = decide_discounts(apple_oatmeal)
        expected[apple_oatmeal_deal] = 1
        self.assertDictEqual(discount_list_apple_oatmeal, expected, "Actual '{}' != expected '{}'".format(discount_list_apple_oatmeal, expected))

        test_basket.add(apple_order)
        test_basket.add(oatmeal_order)
        apple_oatmeal = test_basket.items_in_total()
        discount_list_apple_oatmeal = decide_discounts(apple_oatmeal)
        expected[apple_oatmeal_deal] = 2
        self.assertDictEqual(discount_list_apple_oatmeal, expected, "Actual '{}' != expected '{}'".format(discount_list_apple_oatmeal, expected))

    def test_transform_discount_tuple(self):
        discounts = {
            ("APOM", "-3.00", "AP1"): 1,
            ("APPL", "-1.50", "AP1"): 2,
            ("CHMK", "-4.75", "MK1"): 1
        }
        actual = transform_discount_tuple(discounts)
        expected = {
            "AP1": [("APPL", "-1.50"), ("APPL", "-1.50"), ("APOM", "-3.00")],
            "MK1": [("CHMK", "-4.75")]
        }
        self.assertDictEqual(actual, expected, "Actual '{}' != expected '{}'".format(actual, expected))

    def test_decide_discounts_order(self):
        bogo_deal = ("BOGO", "-11.23", "CF1")
        apple_deal = ("APPL", "-1.50", "AP1")
        chai_milk_deal = ("CHMK", "-4.75", "MK1")
        apple_oatmeal_deal = ("APOM", "-3.00", "AP1")

        apple_order = ("AP1", "6.00")
        chai_order = ("CH1", "3.11")
        coffee_order = ("CF1", "11.23")
        milk_order = ("MK1", "4.75")
        oatmeal_order = ("OM1", "3.69")

        bogo_discount = ("BOGO", "-11.23")
        apple_discount = ("APPL", "-1.50")
        chai_milk_discount = ("CHMK", "-4.75")
        apple_oatmeal_discount = ("APOM", "-3.00")

        basket_order = [apple_order, apple_order, apple_order]
        discounts = {apple_deal: 3}
        expected = [apple_order, apple_discount, apple_order, apple_discount, apple_order, apple_discount]
        actual = order_discounts(basket_order, discounts)
        self.assertEqual(actual, expected, "Actual '{}' != expected '{}'".format(actual, expected))

        basket_order = [chai_order, apple_order, milk_order]
        discounts = {chai_milk_deal: 1}
        expected = [chai_order, apple_order, milk_order, chai_milk_discount]
        actual = order_discounts(basket_order, discounts)
        self.assertEqual(actual, expected, "Actual '{}' != expected '{}'".format(actual, expected))

        basket_order = [chai_order, apple_order, coffee_order, coffee_order]
        discounts = {bogo_deal: 1}
        expected = [chai_order, apple_order, coffee_order, bogo_discount, coffee_order]
        actual = order_discounts(basket_order, discounts)
        self.assertEqual(actual, expected, "Actual '{}' != expected '{}'".format(actual, expected))

        basket_order = [chai_order, apple_order, oatmeal_order]
        discounts = {apple_oatmeal_deal: 1}
        expected = [chai_order, apple_order, apple_oatmeal_discount, oatmeal_order]
        actual = order_discounts(basket_order, discounts)
        self.assertEqual(actual, expected, "Actual '{}' != expected '{}'".format(actual, expected))

        basket_order = [apple_order, apple_order, chai_order, apple_order, oatmeal_order]
        discounts = {apple_oatmeal_deal: 1, apple_deal: 3}
        expected = [apple_order, apple_oatmeal_discount, apple_order, apple_discount, chai_order, apple_order, apple_discount, oatmeal_order]
        actual = order_discounts(basket_order, discounts)
        self.assertEqual(actual, expected, "Actual '{}' != expected '{}'".format(actual, expected))


if __name__ == "__main__":
    unittest.main()
