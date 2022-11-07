from people.people1 import people1, sum
from Q14 import box
# from 파일 import 기능 이름
# box()
# a = people1("kim", 20)
# print(a.name)
# print(sum(1,2))
# 패키지

# package people:
#     def __init__:
#
#     class people1:
#         class people1: 
#             name =""
#             age =0
#             def __init__(self,_name,_age) -> None:
#                 self.name = _name
#                 self.age = _age
#                 pass 
#          def sum():
from phone.galaxy import galaxy
from phone.iphone import iphone
# a = galaxy("갤럭시 노트 10",1000000,True)
# print(a.sampay)
# print(a.price)
# print(a.name)
# b = iphone("아이폰 13 프로",2000000,False)
# print(b.apppay)
# print(b.price)
# print(b.name)
myphone = iphone("아이폰 xr", 1500000, False)
yourphone = galaxy("s7", 1000000, False)
yourphone2 = iphone("아이폰 11", 1000000, True)
# {}
yourphone.discount(10)
myphone.discount(10)
print(yourphone.price)
print(myphone.price)





