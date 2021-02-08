def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    cache = []
    answer = 0
    for i in cities:
        if i.lower() in cache:
            answer += 1
            cache.pop(cache.index(i.lower()))
            cache.append(i.lower())
        else:
            answer += 5
            if len(cache) == cacheSize:
                cache.pop(0)
            cache.append(i.lower())

    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))