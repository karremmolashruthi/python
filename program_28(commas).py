n=int(input())
digits=len(str(n))
total=0
for i in range(1,digits):
    commas_per_num=(i-1)//3
    how_many_commas=9*(10**(i-1))
    total+=commas_per_num*how_many_commas
commas_per_num=(digits-1)//3
how_many_commas=n-(10**(digits-1))+1
total+=commas_per_num*how_many_commas
print(total)
    
