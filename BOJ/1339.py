N = int(input())
words = [input() for _ in range(N)]

dict = {}
for word in words:
    k = len(word) - 1
    for w in word:
        if w in dict:
            dict[w] += 10 ** k
        else:
            dict[w] = 10 ** k
        k -= 1

nums = sorted([val for val in dict.values()], reverse=True)

ans, cnt = 0, 9
for i in range(len(nums)):
    ans += nums[i] * cnt
    cnt -= 1
print(ans)
