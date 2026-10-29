l=[1,2,3,4,5]
target=7
low=0
high=len(l)-1
while low<high:
    total= l[low]+l[high]
    if total==target:
        print("Target found by adding",l[low],l[high])
        break
    elif total<target:
        low+=1
    else:
        high-=1
