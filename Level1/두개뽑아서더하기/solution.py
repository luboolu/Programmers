def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if j > i:
                answer.append(numbers[i] + numbers[j])

    answer = sorted(list(set(answer)))

    return answer