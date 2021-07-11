def solution(phone_book):
    answer = True
    phone = sorted(phone_book)

    for i in range(len(phone)):
        if i != len(phone) - 1:
            if phone[i] == phone[i + 1][0: len(phone[i])]:
                answer = False
                break

    return answer