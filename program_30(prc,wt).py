n,m=list(map(int,input().split()))
arr=list(map(int,input().split()))
product=[]
for i in range(m):
    price,weight=list(map(int,input().split()))
    product.append([price,weight])
print(product)
ans=[]
for cap in arr:
    total=0
    for prc,wt in product:
        if prc<=cap:
            total+=wt
    ans.append(total)
print(*ans,sep=" ")    
