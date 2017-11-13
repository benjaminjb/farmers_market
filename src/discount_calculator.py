from discounts import discount_list
from collections import defaultdict
import operator


def decide_discounts(basket_amounts):
    """Takes a dictionary of orders, iterates over the discounts and tests against each rule.
    If applicable, adds the discount to the dictionary of applicable discounts,
    decrements the order dictionary, and re-tests.
    Note: Allows for the application of special rules. Currently there is only one special rule,
    so it's made explicit in the code. If other special rules come up, a "special rule applicator"
    could be abstracted as a helper function.

    basket_amounts example: { ("AP1", "6.00"): 2, ("OM1", "3.69"): 1 }
    discount rule example: {
        "items": ("AP1", "6.00"),
        "comparator": ">=",
        "quantity": 1
    }
    output example: { ("APOM", "-3.00", "AP1"): 1 }
    """
    comparator = { ">=": operator.ge }
    counter = basket_amounts.copy()
    applicable_discounts = defaultdict(int)

    for discount in discount_list:
        discount_flag = True
        while discount_flag:
            for rule in discount["rules"]:
                if not comparator[rule["comparator"]](counter[rule["items"]], rule["quantity"]):
                    discount_flag = False
            if discount_flag:
                pared_discount = (discount["name"], discount["credit"], discount["apply_to"])
                if discount.get("special") == "each":
                    applicable_discounts[pared_discount] = counter[rule["items"]]
                    discount_flag = False
                else:
                    applicable_discounts[pared_discount] += 1
                    for rule in discount["rules"]:
                        counter[rule["items"]] -= rule["quantity"]
                    if discount.get("limit") == 1:
                        discount_flag = False

    return applicable_discounts

def order_discounts(basket_order, discounts):
    """Takes a list of orders and a dictionary of discounts, and merges them.

    basket_order example: { ("AP1", "6.00"), ("OM1", "3.69") }
    discounts example: { ("APOM", "-3.00", "AP1"): 1 }
    output example: [ ("AP1", "6.00"), ("APOM", "-3.00"), ("OM1", "3.69") ]
    """
    discount_keyed = transform_discount_tuple(discounts)
    order_and_discounts = []
    for order in basket_order:
        order_and_discounts.append(order)
        possible_discount = discount_keyed.get(order[0], None)
        if possible_discount != None and len(possible_discount) > 0:
            pop_discount = possible_discount.pop()
            order_and_discounts.append(pop_discount)
    return order_and_discounts

def transform_discount_tuple(discounts):
    """Takes a dictionary of discounts (with counts), and transforms them,
    making a key of the item-to-apply.
    Note: Allows multiple types of discounts for a single item type,
    but sorts discounts so that largest discount will end up being applied first.

    discounts example: { ("APOM", "-3.00", "AP1"): 1 }
    output example: { "AP1": [("APOM", "-3.00") ] }
    """
    discount_keyed = {}
    for tuple_key, value_amt in discounts.items():
        item = tuple_key[2]
        deals = [(tuple_key[0], tuple_key[1]) for ind in range(value_amt)]
        if discount_keyed.get(item):
            discount_keyed[item] = sorted((discount_keyed[item] + deals), key=lambda d: d[1])
        else:
            discount_keyed[item] = deals
    return discount_keyed
