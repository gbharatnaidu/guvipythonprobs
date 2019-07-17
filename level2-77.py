n=int(input())
count=1
k=[]
a=list(map(int,input().split()))
for i in range(0,len(a)-1):
    if a[i]<a[i+1]:
        count=count+1
    else:
        k.append(count)
        count=1
k.append(count)
print(max(k))
