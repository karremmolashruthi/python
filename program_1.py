n=int(input())
k=int(input())
arr=list(map(int,input().split()))
ans=0
for i in range(n-k+1):
    sub_arr=arr[i:i+k]
    print("find the score for sum sub arr",sub_arr)
    sum=0
    for ind in range(1,k+1):
        sum+=sub_arr[ind-1] * ind
        print("sum is",sum)
    print("score is:",sum)    
    if sum>ans:
        ans=sum
print(ans)            
    
