T=int(input())
for tc in range(1,T+1):
    li=list(input())
    card=[li[i:i+3] for i in range(0,len(li),3)]

    flag=False
    for i in range(len(card)):
        for j in range(i+1,len(card)):
            if card[i] == card[j]:
                print('#{} ERROR'.format(tc))
                flag=True
                break

    cnt_s=cnt_d=cnt_h=cnt_c=13
    for i in range(len(card)):
        if card[i][0] == 'S':
            cnt_s -=1
        if card[i][0] == 'D':
            cnt_d -=1
        if card[i][0] == 'H':
            cnt_h -=1
        if card[i][0] == 'C':
            cnt_c -=1
    if flag == False:
        print('#{} {} {} {} {}'.format(tc,cnt_s,cnt_d,cnt_h,cnt_c))