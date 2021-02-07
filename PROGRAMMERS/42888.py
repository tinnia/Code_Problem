def solution(record):
    answer = []
    nick = {}
    for i in [i.split(' ') for i in record]:
        if i[0] != 'Leave':
            nick[i[1]] = i[2]

    for i in [i.split(' ') for i in record]:
        if i[0] == 'Enter':
            answer.append(nick[i[1]] + "님이 들어왔습니다.")
        if i[0] == 'Leave':
            answer.append(nick[i[1]] + "님이 나갔습니다.")
    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))