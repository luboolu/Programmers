def solution(s):
    answer = ''
    num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    numbers = []

    tmp = ''
    for i in s:
        if i.isalpha():
            tmp += i

            if tmp in num:
                numbers.append(tmp)
                tmp = ''
        else:
            numbers.append(i)

    for n in numbers:
        if n in num:
            answer += str(num.index(n))
        else:
            answer += str(n)

    return int(answer)