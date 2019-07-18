a,b=input().split()
lst=""
if len(a)==len(b):
    print(a,end="")
    print(b)
elif len(a)>len(b):
    for i in range(len(b)):
        lst=lst+a[i]
    print(lst,end="")
    print(b)
else:
    for i in range(len(a)):
        lst=lst+b[i]
    print(a,end="")
    print(lst)
