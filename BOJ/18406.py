N = list(input())
N = [int(i) for i in N]
if sum(N[:len(N)//2]) == sum(N[len(N)//2:]):
    print('LUCKY')
else:
    print('READY')