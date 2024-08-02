n=int(input())
arr=list(map(int,input().split()))
count={}
for i in arr:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)
newArr=[]
for i,freq in count.items():
    newArr+=[freq]*i
print(sorted(newArr))
