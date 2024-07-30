def isPrime(n):
    if n in (0,1):
        return False
    else:
        for i in range(2,int(n**0.5)+1): #n**0.5->returns float num so convert into int 
            if n%i==0:
                return False
        return True
n=int(input())
nextNum=n+1
while True:
    if isPrime(nextNum):
        print(nextNum)
        break
    nextNum+=1
