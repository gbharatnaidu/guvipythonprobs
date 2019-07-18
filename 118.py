s=input().split()
lst=[]
for x in s:
    lst.append(len(x))
for i in range(len(lst)):
    if max(lst)==lst[i]:
        k=i
        break
print(s[k])
