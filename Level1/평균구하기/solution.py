def solution(arr):
    answer = 0
    sum = 0
    for a in arr:
        sum += a

    answer = sum / len(arr)

    return answer