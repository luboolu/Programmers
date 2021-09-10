def solution(info, query):
    answer = []
    # 지원자 정보
    applicant = []
    for i in info:
        split_i = i.split(" ")
        applicant.append(
            {"lang": split_i[0], "jd": split_i[1], "career": split_i[2], "food": split_i[3], "score": int(split_i[4])})

    # print(*applicant, sep = "\n")

    # 문의 조건
    querys = []
    for q in query:
        # split_q = q.split("and")
        split_q = q.split(" ")
        print(split_q)
        split_q = [i for i in split_q if i != "and"]
        print(split_q)
        print()
        querys.append(
            {"lang": split_q[0], "jd": split_q[1], "career": split_q[2], "food": split_q[3], "score": int(split_q[4])})

    print(*querys, sep="\n")

    # print([k for k, v in applicant[0].items() if v == 'java'])

    print(applicant[0]['lang'])

    return answer