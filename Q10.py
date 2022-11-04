
# (클래스 class) (oop 객체지향 )
a = []

# class 여러개의 기능 가지고 있는거 
# python 에서는 @ 데코레이션 
# @overload
# overload 하나의 이름으로 변수에따라 기능이 달라질 수 있다

# @overload
# def sum(a:int):
#     return a

# @overload
# def sum(a:str):
#     return a
# default 기본값
# print({"name":"kim"}.get("age","없어")) 
# -> None

# print({"name":"kim"}.get("name" ,"없어")) 
# -> kim
# @final
# range(start, stop [, step])
# @overload
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# def range(start, end):
#     i=start
#     a=[]
#     while i!=end:
#         a.append(i)
#         i+=1
#     return a
# @overload
# def range(start, end, step=1):
#     i = start
#     a = []
#     while i <= end:
#         a.append(i)
#         i+=step
#     return a

# print(range(0, 10))
# for i in range(0,5,2):
#     print(i)

# class 여러개의 기능 가지고 있는거 

# open input
# num = input("숫자를\t입력해줘\n") # "1"
# num1 = input("숫자를\t입력해줘\n") # "2"
# print("print", int(num)+int(num1)) 
# num+num1 -> "1"+"2"-> "12"
# int(num)+int(num1) -> 1 + 2-> 3
# while True:
#     num = input()

# open 파일 오픈 
# open -> 쓰고 읽고 저장


# def sum(a=0,b=0,c=0,type="sum"):
#     if type =="sum":
#         return a+b+c
#     else:
#         return a-b-c
        

# print(sum(a=1,b=2,type="ss"))

# f = open("test.txt","w")
# # input("입력 : \n") -> "end"
# # 끝나게
# while True:
#     st = input("입력 : \n")
#     if st=="end":
#         break
#     f.write(st+"\n")
# f.close()

# f = open("test.txt","r")
# for line in f.readlines():
#     print(line.strip())
# f.close()
# 연결해서 쓰는거
# csv에서 데이터 만드는거 해보고

# 연결해서 쓰는거
# f = open("test.txt", "w", encoding="utf-8")
# f.write("글을 쓴다")
# f.close()

# f = open("test.txt","a", encoding="utf-8")
# f.write("글을 쓴다 2")
# f.close()

# write read append
# 한글 깨지면 encoding="utf-8"
# 파일은 닫아줘라 f.close()

# {"name": "kim", "age": 15}
f = open("9898.csv", "r", encoding="utf-8")
total_data = f.readlines()
data_keys = total_data[0].strip().split(",")

# for i in range()
data1 = total_data[1].strip().split(",")
dict1 = {data_keys[0]: data1[0]
, data_keys[1]: data1[1] }
print(dict1)
# total_data[2]
# 'park,18\n' strip -> 'park,18'
# 'park,18' split(",") -> ['park','18']
data2 = total_data[2].strip().split(",")
dict2 = {data_keys[0]: data2[0]
, data_keys[1]: data2[1] }
print(dict2)

f.close()



























