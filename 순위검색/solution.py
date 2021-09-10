def solution(info, query):
    answer = []
    # 지원자 정보
    applicant = []
    for i in info:
        split_i = i.split(" ")
        applicant.append(split_i)
        # applicant.append({"lang": split_i[0], "jd": split_i[1], "career": split_i[2], "food": split_i[3],"score": int(split_i[4])})

    print(*applicant, sep="\n")

    # 문의 조건
    querys = []
    for q in query:
        split_q = q.split(" ")
        split_q = [i for i in split_q if i != "and"]
        querys.append(split_q)
        # querys.append({"lang": split_q[0], "jd": split_q[1], "career": split_q[2], "food": split_q[3],"score": int(split_q[4])})

    print()
    print(*querys, sep="\n")

    # print([k for k, v in applicant[0].items() if v == 'java'])

    for q in querys:
        num = 0
        for a in applicant:
            if q[0] != "-" or q[0] == a[0]:
                if q[1] != "-" or q[1] == a[1]:
                    if q[2] != "-" or q[2] == a[2]:
                        if q[3] != "-" or q[3] == a[3]:
                            if q[4] != "-" or q[4] == a[4]:
                                num + 1

        answer.append(num)

    return answer