def solution(a, b):
    answer = 0
    if a == b:
        answer = a
    elif a < b:
        while a <= b:
            answer += a
            a += 1
    else:
        while a >= b:
            answer += b
            b += 1

    return answer