T = 1
while 1:
    L, P, V = map(int, input().split())
    if L + P + V == 0:
        break
    if V % P < L:
        print(f"Case {T}: {L * (V // P) + V % P}")
    else:
        print(f"Case {T}: {L * (V // P) + L}")
    T += 1
