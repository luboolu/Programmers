def solution(weights, head2head):
    answer = []
    score = []
    # N = none, W = Win, L = Lose
    for i in range(len(weights)):
        s = int(weights[i])
        play = 0
        # print(s)
        for j in range(len(head2head[i])):
            if head2head[i][j] != "N":
                play += 1000000

            if head2head[i][j] == "W":
                if weights[j] > weights[i]:
                    s = s + 1001000
                else:
                    s = s + 1000000
        if play != 0:
            score.append((s / play) * 100)
        else:
            score.append(s)

    sorted_score = sorted(score, reverse=True)
    print(score)
    print(sorted_score)
    for sc in sorted_score:
        answer.append(score.index(sc) + 1)
        score[answer[-1] - 1] = -1

    return answer