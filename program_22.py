arr=list(map(int,input().split()))
sum=0
dist=0
for i in arr:
    sum+=i
    if abs(sum)>dist:
        dist=abs(sum)
print(dist)        
    
