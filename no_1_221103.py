# 배열 움직이기

# [1, 2, 3, 4, 5, 6]
# ["left","right","right","right"]

# "left"
# [2,3,4,5,1]

# "right"
# [1,2,3,4,5,6]

# "right"
# [6,1,2,3,4,5]

# "right"
# [5,6,1,2,3,4]
# [1, 2, 3, 4, 5]
# [2, 3, 4, 5, 1]


# left 실행
# num_list = [1, 2, 3, 4, 5]

# new_num_list = []
# for i in range(0, len(num_list)):
#     if i == (len(num_list)-1):
#         new_num_list.append(num_list[0])
#     else :
#         new_num_list.append(num_list[i+1])

# print(new_num_list)

# right 실행
# [1, 2, 3, 4, 5]
# [5, 1, 2, 3, 4]

# num_list = [1, 2, 3, 4, 5]

# new_num_list = []
# for i in range(0, len(num_list)):
#     if i == 0:
#         new_num_list.append(num_list[len(num_list)-1])
#     else :
#         new_num_list.append(num_list[i-1])
# print(new_num_list)

# [1, 2, 3, 4, 5, 6], ["left", "right", "right", "right"]
def solution(num_list : list[int], direct_list : list[str]) :
    if len(direct_list) == 0 :
        print(f'\n{num_list}')
        return
    new_num_list = []
    if direct_list[0] == "left" :
        for i in range(0, len(num_list)):
            if i == (len(num_list)-1):
                new_num_list.append(num_list[0])
            else :
                new_num_list.append(num_list[i+1])
    elif direct_list[0] == "right" :
        for i in range(0, len(num_list)):
            if i == 0:
                new_num_list.append(num_list[len(num_list)-1])
            else :
                new_num_list.append(num_list[i-1])
    direct_list.remove(direct_list[0])
    solution(new_num_list, direct_list)
    
solution([1, 2, 3, 4, 5, 6], ["left", "right", "right", "right"])

#[1, 2, 3, 4, 5, 6], ["left", "right", "right", "right"]
# num_list_copy= [1, 2, 3, 4, 5, 6]
# num_list_copy= [2, 3, 4, 5, 6, 1]
# num_list_copy= [1, 2, 3, 4, 5, 6]
# num_list_copy= [6, 1, 2, 3, 4, 5]
# num_list_copy= [5, 6, 1, 2, 3, 4]
# def solution(num_list : list[int], direct_list : list[str]) :
#     num_list_copy = num_list.copy()
#     for a in direct_list:
#         new_num_list = []
#         if a == "left" :
#             for i in range(0, len(num_list)):
#                 if i == (len(num_list)-1):
#                     new_num_list.append(num_list_copy[0])
#                 else :
#                     new_num_list.append(num_list_copy[i+1])
#         elif a == "right" :
#             for i in range(0, len(num_list)):
#                 if i == 0:
#                     new_num_list.append(num_list_copy[len(num_list)-1])
#                 else :
#                     new_num_list.append(num_list_copy[i-1])
#         num_list_copy = new_num_list
#     print(num_list_copy)
# solution([1, 2, 3, 4, 5, 6], ["left", "right", "right", "right"])