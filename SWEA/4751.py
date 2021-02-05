T=int(input())
for tc in range(1,T+1):
    N=input()
    arr=[['.'] * (4*len(N)+1) for _ in range(5)]

    for i in range(len(N)):
        arr[2][2+4*i] = N[i]

    for i in range(0,5,4):
        for j in range(2,4*len(N)+1,4):
            arr[i][j] ="#"

    for i in range(1,5,2):
        for j in range(1,4*len(N)+1,2):
            arr[i][j] = "#"

    for i in range(0,4*len(N)+1,4):
        arr[2][i] = "#"
    for i in range(5):
        print(''.join(arr[i]))