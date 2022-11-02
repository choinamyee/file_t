# if 1+1==3: #1
#     print("2")
# elif 1+1==2: #2
#     print("2")
# else : #3
#     print("?")
#  list = 순서가 있고 어떤 형이 들어가든 상관없는거
a = [1,2,3]
a = ["a","b","c"]
a = [{"1":3},{"1":3},{"1":3}]
a = [[1,2,3],[1,2,3],[1,2,3]]
a = [True,False]




# company = "abcdefg"
# flag = True
# for c in company:
#     if c =="e":
#         flag = False
#     if flag:
#         print(c)

# company = "abcdefg"
# for c in company:
#     print(c)
#     if c =="e":
#         break   # 반복문을 끝낸다
#     print(c)


# company = "abcdefg"
# for c in company:
#     print(c)
#     if c =="e":
#         continue   # 반복문
#     print(c)


tmp = {
    0: {"str" : "2 와 3의 공배수가 아닌 것은 ","count": 0}
    ,2: {"str" : "2의 배수 인 것은 ","count": 0}
    ,3: {"str" : "3의 배수 인 것은 ","count": 0}
    ,6: {"str" : "2 와 3의 공배수 인 것은 ","count": 0}
    }
b = [6, 2, 3, 0] # 내일 
a = [47,90,1,23,40,5]
for el in a : # el = 40
    for i in b: # i=6 2 3 0
        if i==0:
            tmp[0]['count'] = tmp.get(0).get('count')+1
            break
        if el % i == 0:
            tmp[i]['count'] = tmp.get(i).get('count')+1
            break

for key in  list(tmp.keys()):
    tmp2 = tmp.get(key) # {"str" : "2 와 3의 공배수가 아닌 것은 ","count": 0}
    print(f"{tmp2.get('str')}{tmp2.get('count')}개입니다")
