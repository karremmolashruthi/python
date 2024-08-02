s=input()
count=0
for i in range(len(s)):
    if i+2<=len(s)-1:
        if s[i]=='H' and s[i+1]=='H' and s[i+2]=='H':
            count+=6
            break
    if s[i]=='H':
        count+=2
    if s[i]=='T':
        count-=1
print(count)        
