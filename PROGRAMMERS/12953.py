def solution(arr):
    answer = 1

    def gcd(n, m):
        while m:
            n, m = m, n % m
        return n

    for i in arr:
        answer *= i // gcd(answer, i)
    return answer
