m,n=map(int,input().split())
lst=input()
lst=lst.split()
lst=list(map(int,lst))
lst1=input()
lst1=lst1.split()
lst1=list(map(int,lst1))
for x in lst1:
  lst.append(x)
lst.sort()
for x in lst:
  print(x,end=" ")
