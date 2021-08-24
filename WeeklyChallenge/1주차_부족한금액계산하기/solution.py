def solution(price, money, count):
    cost = 0

    for c in range(count):
        cost += (c + 1) * price

    if cost > money:
        return cost - money
    else:
        return 0
