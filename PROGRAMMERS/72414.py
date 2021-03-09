# def changeDate(time):
#     time = time.split(':')
#     return int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])
#
#
# def changeTime(time):
#     s = time % 60
#     time //= 60
#     m = time % 60
#     time //= 60
#     return '{:02d}:{:02d}:{:02d}'.format(time, m, s)
#
#
# def solution(play_time, adv_time, logs):
#     if play_time == adv_time:
#         return "00:00:00"
#     else:
#         play, adv = changeDate(play_time), changeDate(adv_time)
#         logs = [[0, 0]] + sorted([[changeDate(log.split('-')[0]), changeDate(log.split('-')[1])] for log in logs], key=lambda x:x[0])
#         time = ans = 0
#         for i in range(len(logs)):
#             st, ed = logs[i][0], logs[i][0] + adv
#             if ed > play:
#                 break
#             now = 0
#             for j in range(len(logs)):
#                 if logs[j][1] < st:
#                     continue
#                 if logs[j][0] > ed:
#                     break
#                 if logs[j][0] >= st and logs[j][1] >= ed:
#                     now += ed - logs[j][0]
#                 elif logs[j][0] < st and logs[j][1] <= ed:
#                     now += logs[j][1] - st
#                 elif logs[j][0] >= st and logs[j][1] <= ed:
#                     now += logs[j][1] - logs[j][0]
#                 else:
#                     now += ed - st
#             if now > ans:
#                 ans = now
#                 time = st
#         return changeTime(time)
def changeDate(time):
    time = time.split(':')
    return int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])


def changeTime(time):
    s = time % 60
    time //= 60
    m = time % 60
    time //= 60
    return '{:02d}:{:02d}:{:02d}'.format(time, m, s)


def solution(play_time, adv_time, logs):
    if play_time == adv_time:
        return "00:00:00"
    else:
        play, adv = changeDate(play_time), changeDate(adv_time)
        plays = [0] * (play + 1)
        for log in logs:
            plays[changeDate(log.split('-')[0])] += 1
            plays[changeDate(log.split('-')[1])] -= 1

        for _ in range(2):
            for i in range(1, play + 1):
                plays[i] += plays[i - 1]

        time = ans = 0
        for i in range(adv, play + 1):
            if time < plays[i] - plays[i - adv]:
                time = plays[i] - plays[i - adv]
                ans = i - adv + 1
        if time <= plays[adv - 1]:
            ans = 0
        return changeTime(ans)


print(solution("02:03:55","00:14:15",["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print(solution("99:59:59","25:00:00",["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
print(solution("50:00:00","50:00:00",["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))