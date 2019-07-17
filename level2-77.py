ax=int(input())
c=1
d=[]
a=list(map(int,input().split()))
for i in range(0,len(a)-1):
    if a[i]<a[i+1]:
        c=c+1
    else:
        d.append(c)
        c=1
d.append(c)
print(max(d))
