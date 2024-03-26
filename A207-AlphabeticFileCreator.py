x=input('Enter the list of words(separate them with a comma)-->')
lst=x.split(',')
 
lst=sorted(lst)

f=open('Alphabetically_sorted_words.txt','w')
f.write((','.join([str(i) for i in lst])))
f.close()
