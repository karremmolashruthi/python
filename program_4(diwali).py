n=int(input())
p=int(input())
time_remaining=240-p
no_prblms=0
for i in range(1,n+1):
    slove_time=5*i
    if slove_time<time_remaining and time_remaining>0:
        no_prblms+=1
        time_remaining-=slove_time
print(no_prblms)

n=int(input())
print(n*7)
