def solution(priorities, location):
    answer = 0
    while 1:
        m = max(priorities)
        tmp = priorities.pop(0)
        if m == tmp:
            answer += 1
            if location == 0:
                break
            else:
                location -= 1
        else:
            priorities.append(tmp)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
    return answer



print(solution([2,1,3,2],2))
print(solution([1,1,9,1,1,1],0))
print(solution([1,1,2,1,1,8],5))
print(solution([6,1,2,1,1,3],0))