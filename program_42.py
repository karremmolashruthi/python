#prefix suffix balance
n=int(input())
arr=list(map(int,input().split()))
total=sum(arr)
print(total)
ans=[]
left,right=0,0
for i in range(0,n):
    left+=arr[i]
    right=total-left
    value=abs(left-right)
    ans.append(value)
print(ans)   
    
    
