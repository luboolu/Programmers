def solution(weights, head2head):
    answer = []
    score = []
    # N = none, W = Win, L = Lose
    for i in range(len(weights)):
        s = int(weights[i]) * 0.001

        for j in range(len(head2head[i])):
            if head2head[i][j] == "W":
                if weights[j] > weights[i]:
                    s = s + 1001
                else:
                    s = s + 1000
        score.append(s)

    sorted_score = sorted(score, reverse=True)

    for sc in sorted_score:
        answer.append(score.index(sc) + 1)
        score[answer[-1] - 1] = -1

    return answer