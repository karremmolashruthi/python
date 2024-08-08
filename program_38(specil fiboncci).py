num=int(input())
f=[1,1]
for n in range(2,num+1):
    value=(f[n-1]*f[n-1]+f[n-2]*f[n-2])%47
    f.append(value)
print(f[-1])    
