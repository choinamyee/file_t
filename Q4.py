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
person_execl = [["name","age"],["kim",13],["park",15],["lee",16]]
keys = person_execl[0] # ["name","age"]
datas = person_execl[1:] # [["kim",13],["park",15],["lee",16]]
save = []
for data in datas: # 3번 반복 첫번째 일때 ["kim",13]
    tmp = {} # {} {'name': 'kim'} {'name': 'kim', 'age': 13}
    for i in range(0,len(keys)): # [0,1] 2 번 반복 i=0
        tmp[keys[i]] = data[i] 
        # i=0, keys[0] = "name" , data[0] ="kim" {'name': 'kim'}
        # i=1, keys[1] = "age" , data[1] =13 {'name': 'kim', 'age': 13}
    save.append(tmp) # [{'name': 'kim', 'age': 13}]
print(save)

    #     tmp[key] = ""
    # for el in data:
    #     tmp[key] = el
# range(0,len(keys)) = [0,1]