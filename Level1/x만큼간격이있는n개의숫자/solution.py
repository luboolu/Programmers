def solution(x, n):
    answer = []

    if x != 0:
        for i in range(x, x * (n + 1), x):
            answer.append(i)
    else:
        for i in range(n):
            answer.append(x)

    return answer