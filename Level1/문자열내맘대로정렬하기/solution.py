def solution(strings, n):
    answer = []
    key = []

    for i in range(len(strings)):
        strings[i] = strings[i][n] + strings[i]

    strings = sorted(strings)

    for i in range(len(strings)):
        strings[i] = strings[i][1:]

    return strings