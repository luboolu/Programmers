import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        min = heapq.heappop(scoville)

        if min >= K:
            break
        elif len(scoville) <= 1 and min < K:
            answer = -1
            break
        else:
            min_2 = heapq.heappop(scoville)
            new_food = min + min_2 * 2
            heapq.heappush(scoville, new_food)
            answer += 1

    return answer