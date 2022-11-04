# ./csv/9898.csv
# ../csv/9898.csv       상위
# C:\python_q\csv\9898.csv # 절대 경로
# csv\9898.csv # 상대 경로 


# # price 평균보다 높은 사람들 뽑아내기
# f = open("../csv/9898.csv", "r", encoding="utf-8")
# total_data = f.readlines()
# data_keys = total_data[0].strip().split(",")
# data_list = []
# for i in range(1,len(total_data)):
#     data1 = total_data[i].strip().split(",")
#     dict1 = {}
#     for j in range(0,len(data1)):
#         dict1[data_keys[j]] = data1[j]
#     data_list.append(dict1)
# # print(data_list)
# f.close()
# # price 평균보다 높은 사람들 뽑아내기
# # 다 더한거 구하기
# price_sum = 0
# for data in data_list :
#     price_sum += int(data.get("price"))# 100005000
# # total_sum = total_sum+ int(data.get("price"))
# # 평균 구하기
# price_avg = price_sum/len(data_list)
# answer = []
# for data in data_list :
#     if int(data.get("price"))>price_avg:
#         answer.append(data)

# print(answer)






# 데이터 뽑아는거
def make_data(file_name:str,mode:str):
    f = open(file_name, mode, encoding="utf-8")
    total_data = f.readlines()
    data_keys = total_data[0].strip().split(",")
    data_list = []
    for i in range(1,len(total_data)):
        data1 = total_data[i].strip().split(",")
        dict1 = {}
        for j in range(0,len(data1)):
            dict1[data_keys[j]] = data1[j]
        data_list.append(dict1)
    f.close()
    return data_list

def make_data_avg(data_list:list,key:str):
    # 토탈 더하는거
    price_sum = 0
    for data in data_list :
        price_sum += int(data.get(key))# 100005000

    # 평균 구하기
    price_avg = price_sum/len(data_list)
    return price_avg


# 평균 이상인거 
def answer_avg_high(data_list:list,key:str,price_avg:int):
    answer = []
    for data in data_list :
        if int(data.get(key))>price_avg:
            answer.append(data)
    return answer

data_list = make_data("../csv/9898.csv","r")
key = "age"
price_avg = make_data_avg(data_list,key)
print(answer_avg_high(data_list,key,price_avg))


