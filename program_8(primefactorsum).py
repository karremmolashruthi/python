def solve(arr,num):
    primes=[]
    for i in range(2,(n//2)+1):
        while num%i==0:
            primes.append(i)
            num=num//i
    if num>2:
        primes.append(num)
    ans=0
    for i in primes:
        try:
            ans+=arr[i]
        except:
            return 0
    return ans
n=int(input())
if n!=0:
    arr=list(map(int,input().split()))
    num=int(input())
    ans=solve(arr,num)
    print(ans)
else:
    print(-1)
