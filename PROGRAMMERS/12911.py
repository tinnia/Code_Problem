def solution(n):
    ns = bin(n).count("1")
    while 1:
        n += 1
        if bin(n).count("1") == ns:
            break
    return n

print(solution(15))