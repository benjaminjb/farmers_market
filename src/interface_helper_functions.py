from products import products
from discount_calculator import *

def add_to_checkout_basket(basket, item):
    """Adds product details for recognized products to basket.

    basket: instance of Basket
    item: "apples"
    """
    product_names = list(products.keys())
    if item in product_names:
        full_item = products.get(item)
        item_details = (full_item["code"], full_item["price"])
        basket.add(item_details)
    else:
        print('''
Sorry, we don't recognize that product.
Please add one of the following:
    {}\n'''.format(str(product_names)[1:-1]))

def print_basket(basket):
    """Prints basket items in order and total sum."""
    discounts = decide_discounts(basket.items_in_total())
    orders_and_discounts = order_discounts(basket.items_in_order(), discounts)
    sum = 0
    print('''Item                          Price
----                          -----''')
    for line in orders_and_discounts:
        print_line(line)
        sum += float(line[1])
    print("-----------------------------------")
    print("{:35.2f}".format(sum))

def print_line(line):
    """Prints item, with placement of code dependent on whether its an order or a discount."""
    debit = credit = ""
    if line[1][0] == "-":
        credit = line[0]
    else:
        debit = line[0]
    print("{:12}".format(debit) + "{:12}".format(credit) + "{:>11}".format(line[1]))
