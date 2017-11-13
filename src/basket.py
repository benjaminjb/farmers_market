from collections import defaultdict

class Basket(object):
   def __init__(self):
       self.items_ordered = []
       self.items_totaled = defaultdict(int)
   def add(self, item):
       self.items_ordered.append(item)
       self.items_totaled[item] += 1
       return self
   def items_in_order(self):
       return self.items_ordered
   def items_in_total(self):
       return self.items_totaled
