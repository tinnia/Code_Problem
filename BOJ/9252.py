a = input()
b = input()
arr = [[''] * (len(a) + 1) for _ in range(len(b) + 1)]
for i in range(1, len(b) + 1):
    for j in range(1, len(a) + 1):
        if b[i - 1] == a[j - 1]:
            arr[i][j] = arr[i-1][j-1] + b[i - 1]
        else:
            if len(arr[i-1][j]) >= len(arr[i][j-1]):
                arr[i][j] = arr[i-1][j]
            else:
                arr[i][j] = arr[i][j-1]

if len(arr[-1][-1]) == 0:
    print(0)
else:
    print(len(arr[-1][-1]))
    print(arr[-1][-1])
