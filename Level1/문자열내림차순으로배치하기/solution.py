def solution(s):
    answer = ''
    sor = sorted(s)

    for i in range(len(sor)):
        answer += sor[len(sor) - i - 1]

    return answer