#뒤집어 더하기 빼기
a = [77,977,5654]

def solution(numbers:list):
    b = []
    # nums_int =0
    # nums = 0
    # [77,977,5654]
    for nums in numbers:
        nums_re = ""
        nums_str = str(nums)
        count = len(nums_str)
        for i in range(0,count):
            nums_re = nums_re + nums_str[count - (i+1)]# "22"[2]
        nums_int = int(nums_re)
        if nums % 2 == 0:
            b.append(-nums_int)
        else:
            b.append(nums_int)
    sum_num = 0
    for n in b:
        sum_num+= n
    return sum_num

print(solution(a))