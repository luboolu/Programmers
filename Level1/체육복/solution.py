def solution(n, lost, reserve):
    answer = 0

    set_lost = sorted(list(set(lost)))
    set_reserve = sorted(list(set(reserve)))
    lost = []

    ##1. 여벌을 가져왔지만 도난당한 학생을 찾아야함
    for i in range(len(set_lost)):
        if set_lost[i] in set_reserve:
            set_reserve.remove(set_lost[i])
        else:
            lost.append(set_lost[i])

    ##2. 여벌을 나누어 주기 전에 체육 수업에 참여할 수 있는 학생의 수를 계산하자
    answer += n - len(lost)

    ##3. 체육복 여벌을 체격에 맞게 학생들에게 분배
    for i in range(len(lost)):
        tmp1 = lost[i] - 1
        tmp2 = lost[i] + 1

        if tmp1 in set_reserve:
            answer += 1
            set_reserve.remove(tmp1)
        elif tmp2 in set_reserve:
            answer += 1
            set_reserve.remove(tmp2)

    return answer