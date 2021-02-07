def solution(n, words):
    answer = [0, 0]
    cnt = 1
    for i in range(1, len(words)):
        word = words[i]
        cnt %= n
        if (words[i][0] != words[i-1][-1]) or (word in words[0:i]):
            return [cnt + 1, i // n + 1]
        cnt += 1
    return answer


print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
