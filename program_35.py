#pizza party
n,y=list(map(int,input().split()))
while n%y!=0:
    y=y+1
print(y)
numbers=list(map(int,str(y)))
print(numbers)
print(sum(numbers))
