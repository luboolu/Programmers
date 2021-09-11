from itertools import combinations


def solution(nums):
    answer = 0
    combs = list(combinations(nums, 3))

    for c in combs:
        sums = sum(c)
        isPrime = True
        ##sums ** (1 / 2)가 더 빠른 경우도 있음
        for i in range(2, sums):
            if sums % i == 0:
                isPrime = False
                break

        if isPrime == True:
            answer += 1

    return answer