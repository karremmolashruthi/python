#Nearest corner
seat=input()
s=input().split("-")
element=None
for row in s:
    if seat in row:
        element=row
        break
element=element.split()
left_corner=element.index(seat)
right_corner=(len(element)-1)-element.index(seat)
if right_corner==0:
    right_corner=99999
print(min(left_corner,right_corner))

