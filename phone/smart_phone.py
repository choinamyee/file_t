# smart_phone.py

class smart_phone:
    name = ""
    price = 0
    def __init__(self,_name,_price):
        self.name = _name
        self.price = _price
        pass

    def set_name(self, _name):
        self.name = _name

    def set_price(self, _price):
        self.price = _price

    def discount(self, per): # 10% 
        self.price = self.price * ((100-per)/100)