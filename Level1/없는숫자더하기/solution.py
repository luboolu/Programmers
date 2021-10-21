def solution(numbers):
    answer = -1
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for n in numbers:
        if n in nums:
            nums.remove(n)

    answer = sum(nums)

    return answer