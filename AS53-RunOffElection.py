master = [['a','b','c'],['a','b','c'],['b','c','a'],['b','c','a'],['c','b','a']]



numA = 0 
numB = 0
numC = 0
for i in master:
  if i[0] == 'a':
    numA += 1
  elif i[0] == 'b':
    numB += 1
  else:
    numC += 1

if max(numA,numB,numC) >= 0.5 * len(master):
  if numA > numB and numA > numC: w = 'a'
  elif numB > numA and numB > numC: w = 'b'
  else: w = 'c'
  print(f'Winner is {w}')
else:
  if numA < numB and numA < numC: l = 'a'
  elif numB < numA and numB < numC: l = 'b'
  else: l = 'c'
  for q in master:
    if q[0] == l:
      q[0] = q[1]

  numA = 0
  numB = 0
  numC = 0
  for i in master:
    if i[0] == 'a':
      numA += 1
    elif i[0] == 'b':
      numB += 1
    else:
      numC += 1
  if numA > numB and numA > numC: 
    print('Winner is a')
  elif numB > numA and numB > numC: 
    print('Winner is b')
  elif numC > numA and numC > numB:
    print('Winner is c')
  else:
    print('Its a tie')



  
