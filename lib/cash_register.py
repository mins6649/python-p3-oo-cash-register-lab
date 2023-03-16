#!/usr/bin/env python3

class CashRegister:
  def __init__(self, total = 0, discount = 0, items =[], most_recent_item = []):
    self.total = total
    self.discount = discount
    self.items = items
    self.most_recent_item =  most_recent_item

  def add_item(self, title, price, quantity = 1):
    self.total += (price * quantity)
    self.items.append(title)
    self.most_recent_item = (title, price, quantity)
    return self.total

  def apply_discount(self):
    discount = self.discount
    total = self.total
    if not discount:
      print("There is no discount to apply.")
      return
      
    new_total = ((100 - discount)/100) * total
    print(f"After the discount, the total comes to ${new_total}") 
  
  def void_last_transaction(self):
    self.total -= (self.most_recent_item[1] * self.most_recent_item[2])
    self.items.pop()
    return self.total