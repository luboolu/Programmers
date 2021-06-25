def solution(board, moves):
    answer = 0
    moved = []
    n = len(board[0])

    for m in moves:
        for i in range(n):
            if board[i][m - 1] != 0:
                moved.append(board[i][m - 1])
                board[i][m - 1] = 0

                break

    for i in range(len(moved)):
        for j in range(len(moved)):
            if j != len(moved) - 1:
                if moved[j] == moved[j + 1]:
                    moved.pop(j)
                    moved.pop(j)
                    answer += 2
                    break

    return answer