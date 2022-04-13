def solution(a, b):
    answer = ''
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    d = b
    if a != 1:
        for i in range(a - 1):
            d += days[i]

    if d % 7 == 1:
        answer = "FRI"
    elif d % 7 == 2:
        answer = "SAT"
    elif d % 7 == 3:
        answer = "SUN"
    elif d % 7 == 4:
        answer = "MON"
    elif d % 7 == 5:
        answer = "TUE"
    elif d % 7 == 6:
        answer = "WED"
    else:
        answer = "THU"

    return answer