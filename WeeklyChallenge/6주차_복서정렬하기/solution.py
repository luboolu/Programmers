def solution(weights, head2head):
    answer = []
    score = []
    BigWin = []
    result = []
    # N = none, W = Win, L = Lose
    for i in range(len(weights)):
        s = 0
        play = 0
        bigwin = 0
        for j in range(len(head2head[i])):
            if head2head[i][j] != "N":
                play += 1000000

            if head2head[i][j] == "W":
                if weights[j] > weights[i]:
                    s += 1000000
                    bigwin += 1
                else:
                    s += 1000000

        BigWin.append(bigwin)
        if play != 0:
            score.append((s / play) * 100)
        else:
            score.append(s)

        result.append({"i": i + 1, "weight": weights[i], "score": score[i], "bigwin": bigwin})

    result.sort(key=lambda x: x["weight"], reverse=True)
    result.sort(key=lambda x: x["bigwin"], reverse=True)
    result.sort(key=lambda x: x["score"], reverse=True)

    for i in result:
        answer.append(i['i'])

    return answer