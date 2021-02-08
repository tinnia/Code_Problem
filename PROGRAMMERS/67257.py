def func(rule, idx, expression):
    if idx == 2:
        return str(eval(expression))
    if rule[idx] == '*':
        res = eval('*'.join([func(rule, idx + 1, i) for i in expression.split('*')]))
    if rule[idx] == '+':
        res = eval('+'.join([func(rule, idx + 1, i) for i in expression.split('+')]))
    if rule[idx] == '-':
        res = eval('-'.join([func(rule, idx + 1, i) for i in expression.split('-')]))
    return str(res)


def solution(expression):
    answer = 0
    rules = [("*", "+", "-"), ("*", "-", "+"), ("+", "-", "*"), ("+", "*", "-"), ("-", "+", "*"), ("-", "*", "+")]

    for rule in rules:
        answer = max(answer, abs(int(func(rule, 0, expression))))

    return answer

print(solution("50*6-3*2"))
