def solution(P):
    answer = ''

    balence, i = isBalenced(P)

    if balence == True:
        return P
    else:
        u = P[:i]
        v = P[i:]

        print(u, "---", v)

    return answer


def isBalenced(P):
    balence = 0
    isBalence = True

    for i in range(len(P)):
        if P[i] == "(":
            balence += 1
        else:
            balence -= 1

        if balence < 0:
            isBalence = False
            return isBalence, i

    return isBalence, 0

