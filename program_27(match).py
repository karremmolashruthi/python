n=int(input())
arr=list(map(int,input().split()))
a,b=0,0
for num in arr:
    if num%2==0:
        if arr.count(num)%2==0:
            a+=1
        else:
            b+=1
    else:
        if arr.count(num)%2==0:
            b+=1
        else:
            a+=1
if a==b:
    print("T 0")
elif a>b:
    print(f"A {a}")
else:
    print(f"B {b}")
    
