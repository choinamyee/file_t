#galaxy.py

class galaxy:
    sampay = False
    name = ""
    price = 0
    def __init__(self, _name, _price,_sampay=True):
        self.sampay = _sampay
        self.name = _name
        self.price = _price
        pass
    