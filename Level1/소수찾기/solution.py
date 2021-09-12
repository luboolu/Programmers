def solution(n):
    answer = 0
    ##소수를 찾는 3가지 방법에 대해서 알아둘것
    p = [True] * (n + 1)

    for i in range(2, int(n ** 0.5) + 1):
        if p[i] == True:
            for j in range(i + i, n + 1, i):
                p[j] = False

    answer = len([i for i in range(2, n + 1) if p[i] == True])

    return answer


