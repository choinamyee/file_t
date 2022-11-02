# while 
# while ~ 동안 반복문
# i=0
# while i < 5: # i=0 1 2 3 4
#     if i==3:
#         break
#     print(i)
#     i = i + 1

# print("끝이다")
# i = 0
# while True:
#     if i % 2 ==0:
#         print(i)    
#     i += 1





# a = [1,3,5,7,9,10,11,13]
# for num in a:
#     if num % 2 ==1:
#         print(num)
# for i in range(0,len(a)):
#     if a[i] % 2 ==1:
#         print(a[i])



# a = [0,1,3,5,7,9,10,11,13]
# i = 0
# while i < len(a):
    
#     if a[i] == 0:
#         i += 1
#         continue

#     if a[i] % 2 == 1:
#         print(f"{a[i]} 홀수") 
#     elif a[i] % 2 == 0:
#         print(f"{a[i]} 짝수") 

#     i+=1 
# match case 뭔가 매치되다 같다  
# if



# a = [0,1,3,5,7,9,10,11,13]
# i = 0
# while i < len(a):
#     flag = "짝수"
#     if a[i] % 2 ==1:
#         flag = "홀수"
#     match flag :
#         case "홀수":
#             print(f"{a[i]} {flag}") 
#         case "짝수":
#             print(f"{a[i]} {flag}") 
#     i+=1 

# 람다 
# map
# map list를 새로운 list 로 만든다
# a = [0,1,3,5,7,9,10,11,13]
# b = [0,2,6,10,14,18,20,22,26]
# c = []
# for i in range(0,len(a)):
#     c.append(a[i]*1)
# print(c)

# reduce
# 합을 구할 때 
# a = [0,1,3,5,7,9,10,11,13]
# b = [0,2,6,10,14,18,20,22,26]
# c = 0
# for i in range(0,len(a)):
#     c += a[i]
# print(c)


# filter
# 필터링 
a = [0,1,3,5,7,9,10,11,13]
b = [1,3,5,7,9,11,13]
c = [] # a에 있는 홀수만 
for i in range(0,len(a)):
    if a[i] % 2 == 1:
        c.append(a[i])
print(c)
    









