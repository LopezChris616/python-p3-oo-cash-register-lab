#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0, total=0, items=[], last_item=0):
    self.discount = discount
    self.total = total
    self.items = []
    self.last_item = last_item

  def add_item(self, item, price, quantity=1):
    self.total += price * quantity
    for amount in range(quantity):
      self.items.append(item)

    self.last_item = price*quantity

  def apply_discount(self):
    if self.discount > 0:
      to_decimal = self.discount / 100
      discounted_amount = self.total * to_decimal
      discounted_total = self.total - discounted_amount
      self.total = discounted_total
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    self.total -= self.last_item
    self.items.pop()
