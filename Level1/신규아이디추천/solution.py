def solution(new_id):
    answer = ''
    new_id = new_id.lower()

    for i in new_id:
        if i.isalpha() or i.isdigit() or i == '-' or i == '_' or i == '.':
            answer += i

    while '..' in answer:
        answer = answer.replace('..', '.')

    if answer[0] == '.':
        if len(answer) > 1:
            answer = answer[1:]

    if answer[-1] == '.':
        answer = answer[:-1]

    if answer == '':
        answer = 'a'

    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    while len(answer) < 3:
        answer += answer[-1]
    return answer