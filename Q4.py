# 반복문
# a = [10,20,30,10,20,30,10,20,30]
# for i in range(0,len(a),-1):
#     print(i)
# #i=i-1
# a = [5,8,7,9,10]
# for i in range(0,len(a)):
#     if a[i] % 2 ==0:
#         print(f"{a[i]} 짝수")
#     else:
#         print(f"{a[i]} 홀수")
    # print(i)
# i index
# el element
# a[index]
# a = [5,8,7,9,10]
# print(list(range(0,len(a), 2)))
# # for i in range(0,len(a)):
# for el in a:
#     if el % 2 ==0:
#         print(f"{el} 짝수")
#     else:
#         print(f"{el} 홀수")

# 반복문
a = [10,20,30,10,20,30,10,20,30]
# for 변수 in 리스트 :
# for i in a:
#     print(i)
# 20 <=  <30
# range(20, 23, 1)
# a = [20,21,22]
# 20 <= 20, 20+3 <23
# range(20, 23, 2)
# a = [20,22]
# [20, 20+(-2*1),20+(-2*2),20+(-2*3),]
# [20, 18, 16, 14, 12, 10, 8, 6, 4, 2]
# 20>= i > 2
# range(start, stop[, step])
# print(list(range(20, 2,-2)))
# for 변수 in 리스트 :
# for i in range(20, 11,-2):
#     print(i)

# print("*")
# print("**")
# print("***")
# print("****")
# print("*****")
# print(list(range(1,6)))

# for i in range(5,0,-1):
#     print("*"*(i))
# person = {"name":"kim","age":13 }
# person1 = {"name":"park","age":15 }
# person2 = {"name":"lee","age":16 }
# a = [person,person1,person2]

# 1.
# person_execl = [["name","age"],["kim",13],["park",15],["lee",16]]
# keys = person_execl[0] # ["name","age"]
# datas = person_execl[1:] # [["kim",13],["park",15],["lee",16]]
# save = []
# for data in datas: # 3번 반복 첫번째 일때 ["kim",13]
#     tmp = {} # {} {'name': 'kim'} {'name': 'kim', 'age': 13}
#     for i in range(0,len(keys)): # [0,1] 2 번 반복 i=0
#         tmp[keys[i]] = data[i] 
#         # i=0, keys[0] = "name" , data[0] ="kim" {'name': 'kim'}
#         # i=1, keys[1] = "age" , data[1] =13 {'name': 'kim', 'age': 13}
#     save.append(tmp) # [{'name': 'kim', 'age': 13}]
# print(save)


# 2.
# person_execl = [["name","age"],["kim",13],["park",15],["lee",16]]
# keys = person_execl[0] # ["name","age"]
# datas = person_execl[1:] # [["kim",13],["park",15],["lee",16]]
# save = []
# for data in datas:
#     tmp = {} # {"name":"","age":""}
#     for key in keys: 
#         tmp[key] = ""
#     for el in data: # ["kim",13]
#         tmp[key] = el
#     save.append(tmp) 
# print(save)

# 3.
# person_execl = [["kim",13],["park",15],["lee",16]]
# save = []
# for data in person_execl: 
#     tmp = {"name":"", "age":0}
#     # tmp1 = tmp.copy()
#     for i in range(0,len(list(tmp.keys()))): 
#         tmp[list(tmp.keys())[i]] = data[i] 
#     save.append(tmp) 
# print(save)
# print(id(save[0]))
# print(id(save[1]))
# print(id(save[2]))

# money = 43250
# if money // 10000 >= 1:
#     print(f"만원 짜리는 {money//10000}개 있고")
#     money -= (money//10000) * 10000
# if money // 5000 >= 1:
#     print(f"5000원 짜리는 {money//5000}개 있고")
#     money = money - (money//5000) * 5000
# else:
#     print(f"5000원 짜리는 없고")
# if money // 1000 >= 1:
#     print(f"1000원 짜리는 {money//1000}개 있고")
#     money = money - (money//1000) * 1000

# money = 43250
# a = [10000, 5000, 1000, 500, 100, 50, 10]
# for won in a :
#     if money // won >= 1:
#         print(f"{won}원 짜리는 {money//won}개 있고")
#         money -= (money//won) * won
#     else:
#         print(f"{won}원 짜리는 없고")

# a = [47,90,1,23,40,5]
# for el in a :
#     answer = f"{el}는 "
#     if el % 2 == 0 and el % 3 == 0:
#         answer += "2 와 3의 공배수 입니다"
#     elif el % 2 == 0 or el % 3 == 0:
#         if el % 2 == 0:
#             answer += "2의 배수 입니다"
#         elif el % 3 == 0:
#             answer += "3의 배수 입니다"
#     else: 
#         answer += "2 와 3의 공배수 아닙니다"
#     print(answer)

# a = [47,90,1,23,40,5]
# count1 = 0
# count2 = 0
# for el in a :
#     if el % 2 ==0:
#         print(f"{el} 은 짝수입니다")
#         count1+=1
#     else:
#         print(f"{el} 은 홀수입니다")
#         count2 = count2 + 1
# print(f"짝수는 {count1}개입니다")
# print(f"홀수는 {count2}개입니다")

a = [47,90,1,23,40,5]
tmp = {
    0: {"str" : "2 와 3의 공배수가 아닌 것은 ","count": 0}
    ,2: {"str" : "2의 배수 인 것은 ","count": 0}
    ,3: {"str" : "3의 배수 인 것은 ","count": 0}
    ,6: {"str" : "2 와 3의 공배수 인 것은 ","count": 0}
    }
# b = [6, 3, 2, 0] 내일 
for el in a :
    answer = f"{el}는 "
    if el % 6 == 0:
        answer += "2 와 3의 공배수 입니다"
        tmp[6]['count'] = tmp.get(6).get('count')+1
    elif el % 2 == 0:
        answer += "2의 배수 입니다"
        tmp[2]['count'] = tmp.get(2).get('count')+1
    elif el % 3 == 0:
        answer += "3의 배수 입니다"
        tmp[3]['count'] = tmp.get(3).get('count')+1
    else: 
        answer += "2 와 3의 공배수 아닙니다"
        tmp[0]['count'] = tmp.get(0).get('count')+1
for key in  list(tmp.keys()):
    tmp2 = tmp.get(key) # {"str" : "2 와 3의 공배수가 아닌 것은 ","count": 0}
    print(f"{tmp2.get('str')}{tmp2.get('count')}개입니다")






