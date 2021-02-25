def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    camera, answer = -30000, 0
    for route in routes:
        if camera < route[0]:
            answer += 1
            camera = route[1]
    return answer


print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))
