a=input()
s=input()
total_cost=0
for i in a:
    if i not in s:
        distance=9999
        for j in s:
            temp_dist=abs(ord(i)-ord(j))
            if temp_dist<distance:
                distance=temp_dist
        total_cost+=distance
print(total_cost)        
