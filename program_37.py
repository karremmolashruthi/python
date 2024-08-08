#fellis function
num=int(input())
f=[1,1]
for n in range(2,num+1):
    value=int(f[n-1]+7*f[n-2]+(n/4))%(10**9+7)
    f.append(value)
print(f[-1])    
