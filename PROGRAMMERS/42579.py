from collections import defaultdict


def solution(genres, plays):
    many, gen = defaultdict(int), defaultdict(list)
    for i in range(len(genres)):
        many[genres[i]] += plays[i]
        gen[genres[i]].append([i, plays[i]])
    many = sorted(many.items(), key=lambda x: x[1], reverse=True)
    answer = []
    for i in many:
        tmp = sorted(gen[i[0]], key=lambda x: x[1], reverse=True)
        if len(tmp) >= 2:
            for j in range(2):
                answer.append(tmp[j][0])
        else:
            answer.append(tmp[0][0])

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop", "aaa"], [500, 600, 150, 800, 2500, 40000]))
