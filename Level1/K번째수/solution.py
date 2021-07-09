def solution(array, commands):
    answer = []

    for i in range(len(commands)):

        arr = array[commands[i][0] - 1: commands[i][1]]
        arr = sorted(arr)

        if len(arr) <= commands[i][2]:
            answer.append(arr[-1])
        else:
            answer.append(arr[commands[i][2] - 1])

    return answer