# 문자열 변환 
# zero = 0
# one = 1
# two = 2
# three = 3
# four = 4
# .
# .
# .
# nine = 9

# 0 ~ 9

# one4seveneight -> 1478
# 2three45sixseven -> 234567
# 23four5six7 -> 234567

def solution(st: str):
    tmp = {
        "zero":0, "one":1, "two":2, "three":3, "four":4,
        "five":5, "six":6, "seven":7, "eight":8, "nine":9
    }
    a, b = [], ""
    for i in st:
        is_num = False
        try:
            int(i)
            is_num = True
        except:
            is_num = False
        if is_num:
            a.append(i)
        else :
            b+=i
            if tmp.get(b) != None:
                a.append(tmp.get(b))
                b=""

    answer = ""
    for s in a :
        answer+=str(s)
    return int(answer)

print(solution("one4seveneight"))
print(solution("2three45sixseven"))
print(solution("23four5six7"))

# print("ab".join(["1","2","3"]))
# print(int("3"))