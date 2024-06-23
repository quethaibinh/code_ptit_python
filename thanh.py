a,K,N = map(int,input().split())
ketqua=[]
check = False
for b in range(1,N - a + 1):
    if a+b<=N and (a+b)%K==0:
        ketqua.append(b)
        check = True
print(*ketqua if check else -1)