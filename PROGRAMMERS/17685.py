# def solution(words):
#     answer = 0
#     for word in words:
#         i = 1
#         while 1:
#             if i == len(word):
#                 answer += i
#                 break
#             cnt = 0
#             for w in words:
#                 if word[:i] == w[:i]:
#                     cnt += 1
#                     if cnt > 1:
#                         break
#             if cnt == 1:
#                 answer += i
#                 break
#             i += 1
#     return answer



def solution(words):
    trie = {}
    for word in words:
        tmp = trie
        for w in word:
            tmp.setdefault(w, [0, {}])
            tmp[w][0] += 1
            tmp = tmp[w][1]

    ans = 0
    for word in words:
        tmp = trie
        for i in range(len(word)):
            if tmp[word[i]][0] == 1:
                break
            tmp = tmp[word[i]][1]
        ans += i + 1
    return ans





print(solution(["go","gone","guild"]))
print(solution(["abc","def","ghi","jklm"]))
print(solution(["wo", "word", "work"]))
print(solution(["wo", "word", "work"]))