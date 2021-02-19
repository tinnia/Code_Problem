N = int(input())
problem = input()
answer = bonus = 0
for i in range(len(problem)):
    if problem[i] == 'X':
        bonus = 0
    else:
        answer += i + 1 + bonus
        bonus += 1

print(answer)