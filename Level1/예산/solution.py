def solution(d, budget):
    answer = 0
    sor = sorted(d)

    for a in sor:
        if a <= budget:
            answer += 1
            budget -= a
        else:
            break

    return answer