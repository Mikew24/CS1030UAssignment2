# By: Aidan Fitzsimmons and Michael Waldron
# 100657364(Aidan)+100657864(Michael)
#Assignment #2 Algorithms and Data Structures :
#This assignment explores data structures such as stacks and functions while also showing us how to converts
# an algorithm on described through text into functional working code
"""
**********************
      Question 1
**********************
                    """
#Creating a working stack class
class Stack:
    # Constructor
    # variable is a integer array
    # Used Can be changed by other functions
    def __init__(self):
        self.stacks = []


        # returns the last item in the stack

    # Also known as the top of the stack of elements
    # if the stack is 0 in length then it returns the only element
    def top(self):
        if len(self.stacks) == 0:
            return self.stacks[0]
        return self.stacks[-1]


        # returns The top most element of stack

    # and removes it from the stack array
    def pop(self):
        return self.stacks.pop()


        # push function adds an element onto the stacks

    # it takes the given number and adds to the end or on the top
    # of the stack
    def push(self, num):
        self.stacks.append(num)

    # checks to see if the stack is empty
    # if it is return true if not return false
    def isEmpty(self):
        if (self.stacks == []):
            return True
        else:
            return False

            # returns everthing that is in the stack
            # But as a string

    def __str__(self):
        return str(self.stacks)


"""
**********************
      Question 2
**********************
                    """


# Creates a new Stack called palindrome
# intializes variable newstring for checking words backwords
# pushes each letter of the string onto the stack
# Then pops eachletter into the newstring variable and out of the stack
# Therefore when it is its new string it has reversed it
# Checks to see if the newstring is the same as the old string
# returns true if so and false if not
def isPalindrome(string):
    palindrome = Stack()
    newstring = ''
    for x in range(0, len(string)):
        palindrome.push(string[x])
    for x in range(len(string), 0, -1):
        newstring = newstring + palindrome.pop()
    if (newstring == string):
        return True
    else:
        return False


"""
**********************
      Question 3
**********************
                    """
#creating a function that will convert and compute a string given in Reverse Polish Notation
def toInteger(str):
    return int(str)

def isInteger(str):
    for chr in str:
        if(chr<'0' or chr>'9'):
         return False
    return True

def calculateRPN(k):
    numbers=Stack()
    #currenttoken is a string that stores the number and keeps adding to it until a space is occupying k[x]
    currentToken = ''
    for x in range(0,len(k)):
        #makes sure k[x] isnt a space

        if(k[x]!=' '):
            #checks if k[x] is a integer

         if(isInteger(k[x])):
             #adds k[x] to the end of the current token string if it is a integer
            currentToken=currentToken+k[x]

        if(k[x]==' 'and currentToken!=''):
            # pushes the current token in integer form onto the top of the stack and resets current token to nothing
            numbers.push(toInteger(currentToken))
            currentToken=''

        if(k[x]!=' 'and isInteger(k[x])==False)   :
            # last checks if its a operator then pops two numbers off the stack then applies the k[x] operator to them
             temp=numbers.pop()
             temp2=numbers.pop()
             if(k[x]=='+'):numbers.push(temp2 + temp)
             if (k[x] == '-'): numbers.push(temp2 - temp)
             if (k[x] == '*'): numbers.push(temp2 * temp)
             if (k[x] == '/'): numbers.push(temp2 / temp)

    # after the forloop finishes the only thing left on the stack is the answer
    print('Answer:',numbers.pop())


