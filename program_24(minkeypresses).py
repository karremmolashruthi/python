number=input()
i=0
count=0
n=len(number)
print(n)
while i<n:
    if i<n-1 and number[i]=='0' and number[i+1]=='0':
        count+=1
        i+=2
    else:
        count+=1
        i+=1
print(count)        
