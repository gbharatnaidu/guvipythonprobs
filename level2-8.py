n=int(input())
lst=input()
lst=lst.split()
lst=list(map(int,lst))
for i in range(n-1):
  if(lst[i]>lst[i+1]):
    print(lst[i],end=" ")
  else:
    print(lst[i+1],end=" ")
