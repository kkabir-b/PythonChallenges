def encode(word):
  return_str=''
  vowel=['a','e','i','o','u']
  for i in word:
    if i.lower() not in vowel and i!=' ':
      return_str+=i+'o'+i
    else:
      return_str+=i 
  print(return_str)
encode('Hello world')
