def solution(info, query):
    answer = []
    # 지원자 정보
    applicant = []
    for i in info:
        split_i = i.split(" ")
        applicant.append(split_i)

    # 문의 조건
    querys = []
    for q in query:
        split_q = q.split(" ")
        split_q = [i for i in split_q if i != "and"]
        querys.append(split_q)

    for q in querys:
        num = 0
        for a in applicant:
            if q[0] == "-" or q[0] == a[0]:
                if q[1] == "-" or q[1] == a[1]:
                    if q[2] == "-" or q[2] == a[2]:
                        if q[3] == "-" or q[3] == a[3]:
                            if q[4] == "-" or int(q[4]) <= int(a[4]):
                                num += 1

        answer.append(num)

    return answer

#
# def solution(info, query):
#     answer = []
#     # 지원자 정보
#     applicant = []
#     for i in sorted(info):
#         split_i = i.split(" ")
#         applicant.append(split_i)
#
#     # 문의 조건
#     querys = []
#     for q in query:
#         split_q = q.split(" ")
#         split_q = [i for i in split_q if i != "and"]
#         querys.append(split_q)
#
#     for q in querys:
#         num = 0
#
#         for a in applicant:
#             tmp_a = []
#             for i in range(len(q)):
#                 if q[i] == "-":
#                     tmp_a.append("-")
#                 else:
#                     tmp_a.append(a[i])
#
#             if tmp_a[:4] == q[:4] and int(tmp_a[4]) >= int(q[4]):
#                 num += 1
#         answer.append(num)
#
#     return answer

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])