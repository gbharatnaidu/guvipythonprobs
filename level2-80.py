n=int(input())
lst=input()
lst=lst.split()
lst=list(map(int,lst))
mx=max(lst)
lst.remove(mx)
mn=max(lst)
print(mx-mn)
