class Good:
    type = "Good"
    discount = 0
    tax_rate = 0
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def apply_discount(self):
        discounted_price = self.price - (self.price * self.discount)
        print(f"Discounted price for {self.name} ({self.type}): {discounted_price}")
        return discounted_price
    
    def calculate_tax(self):
        tax = self.price * self.tax_rate
        print(f"Tax for {self.name} ({self.type}): {tax}")
        return tax


class Electronics(Good):
    type = "Electronics"
    discount = 0.10
    tax_rate = 0.15
    
    

class Clothing (Good):
    type = "Clothing"
    discount = 0.20
    tax_rate = 0.08

class Grocery(Good):
    type="Grocery"
    discount = 0.05
    tax_rate = 0.02

