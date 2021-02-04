import sys
input = sys.stdin.readline

def function(n, x, y):
    global result
    if x == r and y == c:
        print(int(result))
        return

    if n == 1:
        result += 1
        return

    if not (x <= r < x + n and y <= c < y+n):
        result += n * n
        return

    function(n/2, x, y)
    function(n/2, x, y+n/2)
    function(n/2, x+n/2, y)
    function(n/2, x+n/2, y+n/2)


N, r, c = map(int, input().split())
result = 0
function(2**N, 0, 0)