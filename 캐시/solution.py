import collections


def solution(cacheSize, cities):
    answer = 0
    cache = collections.deque(maxlen=cacheSize)

    for c in cities:
        c = c.lower()

        if c in cache:
            cache.remove(c)
            cache.append(c)
            answer += 1
        else:
            cache.append(c)
            answer += 5

    return answer