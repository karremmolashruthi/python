arr=list(map(int,input().split()))
target_sum=int(input())
n=len(arr)
for i in range(n-1):
    for j in range(i+1,n):
        if arr[i]+arr[j]==target_sum:
            print([i,j])
            break
