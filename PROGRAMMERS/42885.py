def solution(people, limit):
    answer = 0
    people.sort()
    i, j = 0, len(people) - 1
    while i <= j:
        if people[j] + people[i] <= limit:
            i += 1
        j -= 1
        answer += 1
    return answer