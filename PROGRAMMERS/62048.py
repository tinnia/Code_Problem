def gcd(n, m):
    if n % m == 0:
        return n
    return gcd(m, n % m)


def solution(w, h):
    return w * h - (w + h - gcd(w, h))
