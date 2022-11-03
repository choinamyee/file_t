# 페이지
# 19 페이지
# 1,2,3,4,5,6,7,8,9
# ,10,11,12,13,14,15,16,17,18,19

# 1이 몇번 나오는지 
# 9가 몇번 나오는지 

# 1은 12번, 9는 2
# 300
# 0~9 3,
# 289
# 2, 8, 9



def solution(n:int):
    b = []
    c = []
    count1 = 0
    count9 = 0
    for i in range(0,n+1):
        i = str(i)
        b.append(i)
    for j in range(0,len(b)):
        num = b[j]
        for i in str(num):
            c.append(i)
    for k in range(0,len(c)):
        if c[k] == "1":
            count1 += 1
        elif c[k] == "9":
            count9 += 1
    return f"페이지는 {n} \n1의 개수는 {count1} \n9의 개수는 {count9}"
print(solution(23))
# n=5
# def solution(n:int):
#     ct = [0,0,0,0,0,0,0,0,0,0]
#     #[0,1,2]
#     #[11,12,13]
#     for j in range(0,n):
#         num = j+1
#         # "12"
#         for i in str(num):
#             k = int(i) # 1
#             ct[k] = ct[k] + 1
#     answer =f"페이지는 {n}"
#     #"26"[0] "26"[1]
#     for k in str(n):
#         new_k = int(k)
#         answer+=f"\n{k}의 개수는 {ct[new_k]}"
#     return answer
# print(solution(26))