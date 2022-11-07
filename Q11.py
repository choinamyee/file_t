# 파이썬 
# 특징 
# 동적 타이핑 
# 타입을 안줘도 알아서 선언됨
# a = "code"
# 스크립트 언어
# a = []
# 한줄씩 읽어내려감

# 문자 
# a = "code" 'code'
# 숫자 
# a,b = 1,2
# a+b # 3
# () 튜플 읽기 전용
# {} 딕셔너리 
# 키 : value
# {"age":20}.get("age")
# set {} 중복이 불가 순서 없음
# a = {1,2,3}
# print(a[0])
# [] 리스트 
# 순서 있음
# a = [1,2,3]
# a[0]

# if 만약에
# 만약에 오늘이 일요일이였으면 
# 오늘 쉴텐데
# today = "월요일"
# if today == "일요일" :
#     print("Rest")
# elif today == "토요일":
#     print("Rest")
# elif today == "금요일":
#     print("내일 rest")
# else :
#     print("출근")

# today = "월요일"
# match today:
#     case "월요일":
#         print("출근")
#     case "일요일":
#         print("rest")

# for 반복문 
# 1 <= 변수 < 5
# 5 < 5 False
# for 변수 in range(1,5):
#     print(변수)
# print(list(range(1,5)))
# for 변수 in [1,2,3,4]:
#     print(변수)   
# a = [1,2,3,4]
# for 변수 in a:
#     print(변수)

# while
# i = 0
# while i < 5:
#     print(i)
#     i = i + 1 
# i = 0
# while True:
#     if i==5:
#         break
#     elif i % 3 == 0: #0/3 =0
#         i = i + 1 # i= 0+1 3+1
#         continue
#     print(i) # 1 2 4
#     i = i + 1 # 1+1 2+1 4+1


# 함수 
# def sum(a : int,b : int = 1):
#     return a + b
# try:
#     print(sum("hello"))
# except:
#     print("뭔가 잘못됨")
    
# def sum(*a): # tuple
#     print(a)
# sum(1,2,3,4,5)
# sum(1,2)
# sum(1,2,3)

# def people(**a): # dict
#     print(a)
# people(name="kim", age="20")

# print("hi",1,end="")
# print("hi",2,end="")

# num = input("숫자를 입력해주세요")
# print(num)
# w r a 
# file = open("test1.txt","w")
# file.write("hi")
# file.close()
# file = open("test1.txt","r")
# lines = file.readlines()
# print(lines)
# file.close()
# file = open("test1.txt","a")
# file.write("\nappend")
# file.close()

# file = open("test1.txt","r")
# lines = file.readlines()
# print(lines)
# file.close()

# 경로 

# 절대경로 
# file = open("C:/python_q/test1.txt","r")
# lines = file.readlines()
# print(lines)
# file.close()

# 상대경로
# . = C:\python_q
# ./Q11.py 
# ./test1.txt
# . 내 위치 
# .. 내 위치 하나 위 
# C:\
# file = open("./test1.txt","w")
# file.write("hi")
# file.close()
# file = open("./test1.txt","r")
# lines = file.readlines()
# print(lines)
# file.close()

# import
# import random
# print(random.random())

# class 
# @ 데코레이션 
# overload
# print(list(range(10)))

# print(list(range(0,10,1)))
# @overload
# def sum(a,b):
#     return a+b
# # @overload
# def sum(a):
#     return a

# print(sum(1,2))
























