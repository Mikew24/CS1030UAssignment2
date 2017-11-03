class Stack:
    def __init__(self):
        self.stacks = []

    def top(self):
        return self.stacks[len(self.stacks)]

    def pop(self):
        return self.stacks.pop()

    def push(self, num):
        self.stacks.append(num)

    def isEmpty(self):
        if (self.stacks == []):
            return True
        else:
            return False

    def __str__(self):
        return str(self.stacks)
def toInteger(str):
    return int(str)
def isInteger(str):
    for chr in str:
        if(chr<'0' or chr>'9'):
         return False
    return True
def polnot(k):
    d=Stack()
    currentToken = ''
    for x in range(0,len(k)):

        if(k[x]!=' '):
         if(isInteger(k[x])):
            print('yoooo',k[x])
            currentToken=currentToken+k[x]
        if(k[x]==' 'and currentToken!=''):
            print('pushing:',currentToken)
            d.push(toInteger(currentToken))
            currentToken=''
        if(k[x]!=' 'and isInteger(k[x])==False)   :
             temp=d.pop()
             print('pop', temp)
             temp2=d.pop()
             print('pop', temp2)
             print(k[x])
             if(k[x]=='+'):d.push(temp2 + temp)
             if (k[x] == '-'): d.push(temp2 - temp)
             if (k[x] == '*'): d.push(temp2 * temp)
             if (k[x] == '/'): d.push(temp2 / temp)
    print(d.pop(),'done')
ds='dddsw'
print(isInteger('5'))
polnot('4 14 - 44 -')
