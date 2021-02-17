money = 1000 - int(input())
lst = [500, 100, 50, 10, 5]
answer = 0

for i in lst:
    while money >= i:
        money -= i
        answer += 1

answer += money
print(answer)