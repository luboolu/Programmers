def solution(p):
    answer = ''
    balence = 0
    if p == "":
        return answer
    else:
        for i in p:
            if i == "(":
                balence += 1
            else:
                balence -= 1

    return answer