import random 
lst=[[],[],[],[],[],[],[],[],[],[]]
x=0
for i in lst:
  x+=1
  for y in range(1,11):
    i.append(('Song'+str(y)+' '+'Artist'+str(x)))

last=0
last_2=0
for i in lst:
  for y in i:
    x=random.choice(lst)
    m=random.choice(x)
    while m[-1]==str(last) or m[-1]==str(last_2):
      x=random.choice(lst)
      m=random.choice(x)
    print(m)
    last_2=last
    last=m[-1]
      

