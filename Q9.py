# while 반복문

# i =0
# while i < 5:
#     print(i)
#     i = i + 1

# for j in range(0,5):
#     print(j)
# k = 0
# i = 0
# 5000000 * 10 + 5000000 * 1
# 100000000 * 10
# while k < 100:
#     q = 0
#     # k = 1819 q = 
#     while q < 10:
#         i+=1
#         if k % 2 == 1: # 홀수 
#             q+=1
#             break # 
#         # if k % 10 == 0:
#         #     break
#         print("q",q)
#         q+=1
        
#     print("i",i)
#     print("k",k)
#     k+=1
    
# q = 0
# # k = 1160
# while q < 10:
#     if k % 2 == 1:
#         k += 1
#         continue # 
#     if k % 10 == 0:
#         break
#     print("q",q)
#     q+=1

# p = [4,3,2,1]
# tmp = p[1] # 3
# p[1] = p[2] #[4,2,2,1]
# p[2] = tmp # [4,2,tmp=3,1]
# print(p)

# p = [1,2,3,4,5,6]
# # 3 2 1
# q = 0
# for i in range(0, len(p)):
#     num_max = p[i] # 1
#     for j in range(i+1, len(p)):
#         q=q+1
#         if num_max < p[j]: # 2 3
#             num_max = p[j] # num_max = 3
#             p[i],p[j] = p[j],p[i]
#             #[4,3,2,1]
# print(p,q)

# p = [1,2,3,4,5,6]
# p_len = len(p)
# o = []
# # 6
# for i in range(0, p_len):
#     p_max = max(p)
#     o.append(p_max)
#     p.remove(p_max)
# print(o)


# def sum(a:int,b:int):
#     try: # 예외처리
#         return a+b
#     except: 
#         return "이상한거"

# print(sum(1,2))
# print(sum("hi",2))
# 2,1 [a,b]
# 3,1 [a,b]
# 100, 1 [a,b]
# diff(a-b,b) a = 3 b= 1 -> diff(2,1)=[a,b]
# diff(2,1) => [a,b]
# diff(a-b,b) a = 4 b= 1 -> 
# diff(3,1) = diff(2,1)=[a,b]
# def diff(a,b):
#     if a-b==1:
#         return [a,b]
#     else:
#         return diff(a-b,b) # 재귀 
# # 재귀 자기 자신을 불러오는거 
# print(diff(100,1))
# a = 1
# for i in range(0,5):
#     a = a + a 
#     # 1+1
#     # 2+2
#     # 4+4
#     # 8+8
#     # 16+16
# print(a)

# p = [1,2,3,4,5,6]
# def sort1(target_list:list, return_list:list):
#     if(len(target_list)==0):
#         return return_list
#     p_max = max(target_list)
#     return_list.append(p_max)
#     target_list.remove(p_max)
#     return sort1(target_list, return_list)
# print(sort1(p, []))


# def sum_func(*nums): # tuple
#     i=0
#     for num in nums:
#        i+= num 
#     return i

# print(sum_func(1,2,3,4))
# print(sum_func(1,2,3,4,7,8,9,1))
# print(sum_func(1))

# def person(a, *nums, **info):
#     print(a)
#     print(nums)
#     return info

# print(person("dd",1,2,3,name="park"))



def space_to_list(st:str):
    b= []
    for i in st:
        if i != " ":
            b.append(i)
    return b

a = "a b c"
# print(space_to_list(a)) # ['a','b','c']
b = a.split(" ")
print(b)











