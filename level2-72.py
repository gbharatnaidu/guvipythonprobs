lst=input()
lst=lst.split()
lst=list(map(int,lst))
for i in range(len(lst)-1):
  if(lst[i]<lst[i+1]):
   k=lst[i+1]
   break
print(lst[i+1])
