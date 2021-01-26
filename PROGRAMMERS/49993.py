def solution(skill, skill_trees):
    answer = 0
    for sk in skill_trees:
        skill = list(skill)
        j = 0
        for i in range(len(sk)):
            if sk[i] in skill:
                if sk[i] == skill[j]:
                    j += 1
                    if j == len(skill):
                        answer += 1
                        break
                else:
                    break
            if i == len(sk)-1:
                answer += 1
    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))