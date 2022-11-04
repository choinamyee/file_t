
# import 
import random
from datetime import datetime
# 0*45+1 <= 랜덤*45+1 < 1*45+1
# 1<= 랜덤 <46
# print(datetime.datetime(2022, 11,4).today())
print(datetime.today())
# 1~45 숫자 6개 
def make_six_number():
    lotto = []
    while len(lotto)!=6:
        # str(random.random()*45+1).split(".")[0]
        num = int(str(random.random()*45+1).split(".")[0])
        num_pass = True
        for j in lotto:
            if j == num:
                print("겹침", num)
                num_pass = False
                break
        if num_pass:
            lotto.append(num)
    lotto.sort()
    return lotto
file = open("../csv/lotto.txt","w", encoding="utf-8")
for i in range(0,5):
    lotto = make_six_number()
    for num in range(0,len(lotto)):
        if num == len(lotto)-1:
            file.write(f"{lotto[num]}")
            continue
        file.write(f"{lotto[num]}, ") # 4, 12, 17, 21, 30, 37,
    file.write("\n")
file.write(f"출력시간 : {str(datetime.today()).split('.')[0]}")
file.close()

# 김철수 박김김 
# str(6.631224828091003)
# "6.631224828091003".split(".")
# ["6","631224828091003"][0]
# int(["6","631224828091003"][0])
