def solution(weights, head2head):
    answer = []
    score = []
    # N = none, W = Win, L = Lose
    for i in range(len(weights)):
        s = int(weights[i]) * 0.001
        play = 0
        # print(s)
        for j in range(len(head2head[i])):
            if head2head[i][j] != "N":
                play += 1

            if head2head[i][j] == "W":
                if weights[j] > weights[i]:
                    s = s + 1001
                else:
                    s = s + 1000
        if play != 0:
            score.append(s / (play * 10000))
        else:
            score.append(s)

    sorted_score = sorted(score, reverse=True)
    print(score)
    print(sorted_score)
    for sc in sorted_score:
        answer.append(score.index(sc) + 1)
        score[answer[-1] - 1] = -1

    return answer