def solution(s, n):
    answer = ''

    for i in s:
        if i == " ":
            answer += " "
        else:
            tmp = i
            for N in range(1, n + 1):
                tmp = chr(ord(tmp) + 1)
                if tmp == "[":
                    tmp = "A"
                elif tmp == "{":
                    tmp = "a"

            answer += tmp

    return answer