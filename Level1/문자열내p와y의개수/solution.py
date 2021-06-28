def solution(s):
    answer = True

    p_num = 0
    y_num = 0

    for x in range(len(s)):
        if s[x] == 'p' or s[x] == 'P':
            p_num += 1
        elif s[x] == 'y' or s[x] == 'Y':
            y_num += 1

    if p_num != y_num:
        return False
    else:
        return True

    return True