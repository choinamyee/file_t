#iphone.py
from phone.smart_phone import smart_phone
# import smart_phone
# smart_phone.smart_phone()
# def sum(a):
#     return a+1
# 상속 

class iphone(smart_phone):
    apppay = False
    def __init__(self, _name, _price, _apppay):
        self.apppay = _apppay
        super().set_name(_name)
        super().set_price(_price)
        pass
    