N,K,A=list(map(int,input().split()))
ans=(A+K-1)%N
if ans==0:
    print(N)
else:
    print(ans)
    
