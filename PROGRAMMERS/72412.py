# def solution(info, query):
#     answer = []
#     lst = [[] for _ in range(len(query))]
#     print(query)
#
#     for i in range(len(query)):
#         tmp = query[i].split()
#         for j in range(8):
#             if j == 7:
#                 lst[i].append(int(tmp[j]))
#             elif tmp[j] == 'and' or tmp[j] == '-':
#                 continue
#             else:
#                 lst[i].append(tmp[j])
#     print(lst)
#
#     return answer


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
                   "cpp and - and senior and pizza 250", "- and backend and senior and - 150",
                   "- and - and - and chicken 100", "- and - and - and - 150"]))
