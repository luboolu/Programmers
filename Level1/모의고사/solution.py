def solution(answers):
    answer = []
    one_answer = []
    two_anwer = []
    three_answer = []

    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    one_div = list(divmod(len(answers), len(one)))
    two_div = list(divmod(len(answers), len(two)))
    three_div = list(divmod(len(answers), len(two)))

    one_answer = one * one_div[0] + one[0:one_div[1]]
    two_answer = two * two_div[0] + two[0:two_div[1]]
    three_answer = three * three_div[0] + three[0:three_div[1]]

    one_score = 0
    two_score = 0
    three_score = 0

    for i in range(len(answers)):
        if one_answer[i] == answers[i]:
            one_score += 1
        if two_answer[i] == answers[i]:
            two_score += 1
        if three_answer[i] == answers[i]:
            three_score += 1

    score = [one_score, two_score, three_score]
    max_score = max(score)

    while max_score in score:
        answer.append(score.index(max_score) + 1)
        score[score.index(max_score)] = -1

    return answer