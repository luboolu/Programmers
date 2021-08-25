def solution(N):
    answer = 0
    otf = []
    sum = 0
    for n in range(N):
        tmp = 3 ** n
        sum += tmp

        if N <= sum:
            print(sum, tmp, n)
            break






    return answer

solution(100)