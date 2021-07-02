
def solution(n):
    answer = 0
    div = n ** 0.5

    if div == int(div):
        if n / div == div:
            answer = int((n / div + 1) * (n / div + 1))
    else:
        answer = -1

    return answer