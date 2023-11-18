lst=input('Enter the list')
lst=[i for i in lst]
lst=sorted(lst)
with open("downloadable_file",'x') as file:
  for i in lst:
    file.write(i)
