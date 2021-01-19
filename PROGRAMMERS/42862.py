def solution(n, lost, reserve):
    lost1 = set(lost) - set(reserve)
    reserve1 = set(reserve) - set(lost)
    for i in reserve1:
        if i-1 in lost1:
            lost1.remove(i-1)
        elif i+1 in lost1:
            lost1.remove(i+1)
    return n - len(set(lost1))