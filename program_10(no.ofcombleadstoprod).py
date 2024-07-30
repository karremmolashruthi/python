n=int(input())
arr=list(map(int,input().split()))
arr.sort()
m=int(input())
count=0
i,j,k=0,0,0
while i<n-2:
    j,k=i+1,n-1
    while j<k:
        product = arr[i] * arr[j] * arr[k]
        if product == m:
            count+=1
            j+=1
            k-=1
        elif product<m:
            j+=1
        else:
            k-=1
    i+=1
print(count)    
