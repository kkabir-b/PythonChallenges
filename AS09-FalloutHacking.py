import random
lst=['ansdkn','ads]p[pLSNPCIJKLA','HELLO','ANSOPD{Q.','NUMBER','JkLNXLZZZ XJNCASAXMS MXCNSAA','NOPE','NJAOSDm','NADS:M oaJNK:M','ANOPDKO{XLA','WHY','LAJDSPA','MALES','BYE']
lst_2=['HELLO','NUMBER','NOPE','WHY','MALES','BYE']
for i in lst:
  print(i)
word=random.choice(lst_2) 
c=0 

got=False
while c<5 and got!=True:
  c+=1
  x=0
  ask=input('What is the word?')
  for i in word:
    if i in ask:
      x+=1
  if ask==word:
    print('You have gotten the word')
    got=True
  else:
    print('The likeness is-->',x)


