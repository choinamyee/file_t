# 함수 
# sum(1,2)
# def sum(a:int, b:int): # 매개 변수 
#     try: # 시도하다 
#         return a + b
#     except: # 예외
#         return "이상한 값입니다"
# print(sum(1, 4))
# print(sum("hi", 4)) # 1,2 인수 

# def diff(a:int, b:int): 
#     answer = "" 
#     try:
#         dif = a - b
#         if dif < 0:
#             answer = 0
#         else:
#             answer = dif
#     except:
#         answer = "잘못된거"
#     finally:
#         return answer

# print(diff(diff("hi",3), diff(3,2)))


# def diff(a:int, b:int): 
#     answer = "" 
#     try:
#         dif = a - b
#         if dif < 0:
#             answer = 0
#         else:
#             answer = dif
#     except:
#         answer = "잘못된거"
#     finally:
#         return answer
# def filtering(a:list):
#     c = []
#     for i in range(0,len(a)):
#         if a[i] % 2 == 1:
#             c.append(a[i])
#     return c
# list1 = [0,1,3,5,7,9,10,11,13]
# list2 = [13,9,2,22,4,5,65,32]
# list3 = [90,23,4,634,12,43,82]
# list4 = "100"
# print(filtering(list1))
# print(filtering(list2))
# print(filtering(list3))
# print(filtering(list4)) 

# def sum(*nums):
#     print(type(nums))
#     answer = 0
#     for num in nums:
#         answer = answer + num
#     return answer

# print(sum(1,2,3,4,5,6))
# print(sum(5,6,7))
pe = [] # 전역변수 
def make_profile(**a):
    del a["age"]
    return a
def peoples(*t_peoples) :
    answer = list(t_peoples) # 지역변수 
    for p in t_peoples:
        pe.append(p)
    return answer

peoples(
    make_profile(name="park",age=20, company="naver"),
    make_profile(name="kim",age=20, company="kakao"),
    make_profile(name="lee",age=20, company="쿠팡"),
    )
peoples(
    make_profile(name="park",age=20, company="naver"),
    make_profile(name="kim",age=20, company="kakao"),
    make_profile(name="lee",age=20, company="쿠팡"),
    )
print(pe, "hi")

# 함수 
# 정의할 땐
# def 이름(매개변수):
# def print(st): 
# print("hi") 함수다 "hi" 인수다
# def print(*st) # type(st) = tuple
# print("hi","hello",1,2,3)
# def print(**st) # type(st) = dict
# print(name="kim", age=20)