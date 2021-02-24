N = input()
tmp = '1' * len(N)

if len(N) == 1:
    print(1)
elif int(tmp) <= int(N):
    print(len(N))
else:
    print(len(N) - 1)
