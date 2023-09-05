import random
def insertionSort(l):
  for i in range(1,len(l)):
    curr = l[i]
    j = i - 1

    while j>=0 and curr < l[j]:
      l[j + 1] = l[j]
      j -= 1
      
    l[j + 1] = curr

l = [random.randint(1,1000000) for i in range(9)]
insertionSort(l)
print(l)
