# def func(rule, idx, expression):
#     if idx == 2:
#         return
#     tmp = eval(rule[idx].join([func(rule, idx+1, e) for e in expression.split(rule[idx])]))
#     return tmp
#
# def solution(expression):
#     answer = 0
#     rules = [
#         ("*", "+", "-"),
#         ("*", "-", "+"),
#         ("+", "-", "*"),
#         ("+", "*", "-"),
#         ("-", "+", "*"),
#         ("-", "*", "+")
#     ]
#     for rule in rules:
#         tmp = func(rule, 0, expression)
#         answer = max(answer, abs(tmp))
#
#     return answer
#
# print(solution("50*6-3*2"))
