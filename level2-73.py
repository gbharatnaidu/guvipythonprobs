n, b = map(int, input().split())
lst=input()
lst=lst.split()
lst=list(map(int,lst))
for i in range(0,len(lst)):
  if(lst[i]==b):
    k=i+1
    break
print(k)
