def solution(x):
    tmp = [int(i) for i in str(x)]
    if x % sum(tmp):
        return False
    return True