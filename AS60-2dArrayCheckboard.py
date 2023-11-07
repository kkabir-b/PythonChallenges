def board(n,m):
  lst=[[] for i in range(m)]

  for i in range(len(lst)):
    for x in range(n):
      if (i+x)%2==0:
        lst[i].append('.')
      else:
        lst[i].append('*')
  print(lst)

board(100,25)
    
