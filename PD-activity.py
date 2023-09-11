""" Making Pseudocode real. Create the Pseudocode in Python.
By the way this is NOT a nice way to name your definitions in Python, but it 
lets you get away with it.
pass lets me not code up the function. It's like on a quiz show.
"""

def LEFT(string,length):   
    # returns the left most characters of a string. 
    # I've done this one as an example.
    return string[0:length]

def RIGHT(string,length):
    
    return string[len(string) - length:]

def MID (string,start,end):
    # Returns string from position x, length y. Note that the count starts at 1. 
    return string[start:start + end + 1]
    
def LENGTH (string):
    #Returns the lengths of a string
    return len(string)

def LCASE (string):
# From here on in you need to figure out the parameters and the function.    
    return string.lower()
    
def UCASE(string):
  return  string.upper()

def TO_UPPER(string):
  return string.upper()
 
def TO_LOWER(string):
  #Returns a string in lower case. (

    return string.lower()
 
def NUM_TO_STRING(num):
    return str(num)

def STRING_TO_NUM(string):
    return int(string)

def INT(string):
    return int(string)

def ASC(string):
  return ord(string)
# example function being called    
my_string = MID("hello",2,5)
print(my_string)
