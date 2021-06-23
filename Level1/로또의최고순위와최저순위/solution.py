def solution(lottos, win_nums):
    answer = []
    zero = 0
    win = 0

    for l in lottos:
        if l == 0:
            zero += 1
        elif l in win_nums:
            win += 1

    answer.append(rank(win))
    answer.append(rank(win + zero))
    answer.sort()

    return answer


def rank(num):
    if num == 6:
        return 1
    elif num == 5:
        return 2
    elif num == 4:
        return 3
    elif num == 3:
        return 4
    elif num == 2:
        return 5
    else:
        return 6