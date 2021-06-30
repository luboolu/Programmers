def solution(nums):
    answer = 0
    pocket = len(nums) / 2
    sort = sorted(nums)
    kinds = 1

    for i in range(len(sort)):
        if i != len(sort) - 1:
            if sort[i] != sort[i + 1]:
                kinds += 1

    if kinds >= pocket:
        answer = pocket
    else:
        answer = kinds

    return answer