#maximum pair product
n=int(input())
arr=list(map(int,input().split()))
ans=[]
product=0
for i in range(0,len(arr)+1):
    temp=0
    for j in range(i+1,len(arr)): 
        if arr[i]+arr[j]==18:
            temp=arr[i]*arr[j]
            if temp>product:
                product=temp
                ans=sorted([arr[i],arr[j]],reverse=True)
print(ans)               
            
               
    
    

