file = open('input.txt','r')
lines = file.readlines()

fileClear = open('output.txt','w')
fileClear.write('')
fileClear.close()

fileOutput = open('output.txt','a')

def getIndent(q):
    c = 0
    for i in q:
        if i == ' ': 
            c+=1 
        elif i!= ' ':
            break
    return c

def fixForLoop(q):
    return f'FOR I<-0 TO {q[15:q.find(")")]}'

def fixOutput(q):
    return f'OUTPUT {q[5:-1]}'

def checkOutput(q):
    q.strip()
    return q[:5] == 'print'

def checkFor(q):
    return q[:3] == 'for'

lstOfEnds = []
prevIndent = -100
for q in lines:
    indent = getIndent(q)
    print(q)
    if prevIndent > indent:
        fileOutput.write(' '*indent + lstOfEnds[-1])
        lstOfEnds.pop()

    if checkFor(q):
        fileOutput.write(' '*indent + fixForLoop(q))
        lstOfEnds.append('ENDFOR')
    
    elif checkOutput(q):
        fileOutput.write(' '*indent + fixOutput)

    fileOutput.write('\n')
    prevIndent = indent


        


file.close()
fileOutput.close()

