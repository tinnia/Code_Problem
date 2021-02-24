def solution(begin, target, words):
    if target not in words:
        return 0

    answer = 0
    visit = [0] * len(words)
    stack = [begin]
    while stack:
        tmp = stack.pop()
        if tmp == target:
            return answer

        for i in range(len(words)):
            if visit[i] == 1: continue

            cnt = 0
            for j in range(len(tmp)):
                if words[i][j] != tmp[j]:
                    cnt += 1
                if cnt == 2:
                    break
            if cnt == 1:
                visit[i] = 1
                stack.append(words[i])
        answer += 1


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
