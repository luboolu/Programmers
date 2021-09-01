from collections import deque


def solution(numbers, target):
    answer = 0

    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()

        if y > len(numbers):
            break
        elif x == target and y == len(numbers):
            answer += 1
        queue.append((x + numbers[y - 1], y + 1))
        queue.append((x - numbers[y - 1], y + 1))

    return answer