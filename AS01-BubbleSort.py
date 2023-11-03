import random
lst=[random.randint(1,100) for i in range(9)]
for x in range(9):
  for i in range(len(lst)-1):
    if lst[i]>lst[i+1]:
      x=lst[i]
      y=lst[i+1]
      lst[i]=y
      lst[i+1]=x
print(lst)
