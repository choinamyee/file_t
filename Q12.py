# class 계산기 :
#     def __init__(self, num = 0):
#         self.num = num

#     def sum(self, a):
#         self.num = self.num + a

#     def diff(self, a):
#         self.num = self.num - a
        
# a = 계산기(1)
# a.sum(1)
# print(a.num)
# a.diff(2)

# b = 계산기(2)
# b.sum(1)
# print(b.num)

# c = 계산기()
# print(c.num)



# a = []
# a.append(1)
# print(a)

# b = []
# b.append(2)
# print(b)

# num = 0 # 전역 변수
# def sum(a):
#     num = num + a # 지역 변수 
#     print(num)

# sum(1)


# class 이름:
#     def __init__(self) -> None:
#         self.name = ""

#     def setName(self, name):
#         self.name = name

# a=이름()
# print(a.name)
# a.setName("park")
# print(a.name)

class 사람: 
    name = ""
    age = 0
    def __init__(self,_name,_age) -> None:
        self.name = _name
        self.age = _age
    def print_name(self):
        print(self.name)
    def print_age(self):
        print(self.age)

최남이 = 사람("kim",30)
최남이.name




class 숫자:
    count = 0
    num1 = 0
    def __init__(self, _num1) -> None:
        self.num1 = _num1
        숫자.count = 숫자.count + 1
        pass

num_list = []
# i<10 range(10)[0,1,2,3,4,5,---]
for i in range(10):
    num_list.append(숫자(i))
print(num_list)
# for i in range(0,10,1):
#     print(num_list[i].num1)
print(num_list[0].count)
class 랭지:
    ran = []
    # @overload
    # def __init__(self, _end):
    #     i = 0
    #     while i < _end:
    #         self.ran.append(i)
    #         i = i+1
    #     self.ran
    # @overload
    def __init__(self, _start,_end,_step=1):
        i = _start
        while i < _end:
            self.ran.append(i)
            i = i+_step
        self.ran

# print(랭지(10).ran)
print(랭지(0,10).ran)
# 클래스 객체지향 = oop






