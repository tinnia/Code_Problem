s = input()
word = input()

i = cnt = 0
while i <= len(s):
    if s[i:i+len(word)] == word:
        cnt += 1
        i += len(word)
    else:
        i += 1

print(cnt)