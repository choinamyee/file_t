# ./csv/9898.csv
# ../csv/9898.csv       상위
# C:\python_q\csv\9898.csv # 절대 경로
# csv\9898.csv # 상대 경로 
f = open("../csv/9898.csv", "r", encoding="utf-8")
total_data = f.readlines()
data_keys = total_data[0].strip().split(",")
data_list = []
for i in range(1,len(total_data)):
    data1 = total_data[i].strip().split(",")
    dict1 = {}
    for j in range(0,len(data1)):
        dict1[data_keys[j]] = data1[j]
    data_list.append(dict1)
print(data_list)
f.close()