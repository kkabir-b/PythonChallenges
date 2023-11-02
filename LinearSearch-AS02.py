lst=[1,2,4,3,5,3,4,5,6,7,8,9,6,4]
item=-1
q=False
s=0
for i in lst:
  if i == item:
    print('Found it')
    q=True
    print(s)
    break
  s+=1
if not(q):print('Not found it')
