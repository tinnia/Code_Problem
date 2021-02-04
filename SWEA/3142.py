for tc in range(1,int(input())+1):
    n,m=map(int,input().split())
    print('#{} {} {}'.format(tc,2*m-n,n-m))