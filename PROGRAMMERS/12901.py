def solution(a, b):
    date = {1: 'FRI', 2: 'SAT', 3: 'SUN', 4: 'MON', 5: 'TUE', 6: 'WED', 0: 'THU'}
    day31 = [1, 3, 5, 7, 8, 10, 12]
    day30 = [4, 6, 9, 11]
    day = b
    for mon in range(1, a):
        if mon in day31:
            day += 31
        elif mon in day30:
            day += 30
        else:
            day += 29
    answer = day % 7
    return date[answer]
