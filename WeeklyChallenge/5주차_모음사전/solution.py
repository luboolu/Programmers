def solution(word):
    answer = 0
    nums = ''
    au = ["A", "E", "I", "O", "U"]

    for w in word:
        nums += str(au.index(w) + 1)

    nums = int(nums)
    notIn = ['6', '7', '8', '9', '0']
    dic = []

    for i in range(55556):
        istr = str(i)
        flag = True
        for n in notIn:
            if n in istr:
                flag = False
                break

        if flag == True:
            dic.append(istr)

    dic = sorted(dic)

    return dic.index(str(nums)) + 1