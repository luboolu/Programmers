def solution(numbers, hand):
    answer = ''
    left_loc = '*'
    right_loc = '#'
    keypad = [[1, 4, 7, '*'], [2, 5, 8, 0], [3, 6, 9, '#']]

    for n in numbers:
        if n in keypad[0]:
            answer += "L"
            left_loc = n
        elif n in keypad[2]:
            answer += "R"
            right_loc = n
        else:
            n_xy = location(keypad, n)
            r_xy = location(keypad, right_loc)
            l_xy = location(keypad, left_loc)

            r = abs(n_xy[0] - r_xy[0]) + abs(n_xy[1] - r_xy[1])
            l = abs(n_xy[0] - l_xy[0]) + abs(n_xy[1] - l_xy[1])

            if r > l:
                answer += "L"
                left_loc = n
            elif r < l:
                answer += "R"
                right_loc = n

            else:
                if hand == "right":
                    answer += "R"
                    right_loc = n
                else:
                    answer += "L"
                    left_loc = n

    return answer


def location(key, num):
    for x in range(len(key)):
        for y in range(len(key[x])):
            if key[x][y] == num:
                return [x, y]