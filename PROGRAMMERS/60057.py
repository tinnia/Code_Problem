def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2 + 1):
        ans_tmp = ""
        cnt = 1
        tmp = s[:i]
        for j in range(i, len(s)+i, i):
            if tmp == s[j:j+i]:
                cnt += 1
            else:
                if cnt != 1:
                    ans_tmp = ans_tmp + str(cnt) + tmp
                else:
                    ans_tmp = ans_tmp + tmp
                tmp = s[j:j+i]
                cnt = 1
        answer = min(answer, len(ans_tmp))
    return answer