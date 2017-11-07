# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 10:39:39 2017

@author: aidan
"""


"""
**********************
      Question 1
**********************
                    """
class Stack:
    #Constructor
	#variable is a integer array
	#Used Can be changed by other functions
    def __init__(self):
        self.stacks = []
    
	
    #returns the last item in the stack
	#Also known as the top of the stack of elements
	#if the stack is 0 in length then it returns the only element
    def top(self):
        if len(self.stacks) == 0:
            return self.stacks[0]
        return self.stacks[-1]
    
	
    #returns The top most element of stack
	#and removes it from the stack array
    def pop(self):
        return self.stacks.pop()
    
	
    #push function adds an element onto the stacks
	#it takes the given number and adds to the end or on the top
	#of the stack
    def push(self, num):
        self.stacks.append(num)
        
		
	#checks to see if the stack is empty
	#if it is return true if not return false
    def isEmpty(self):
        if(self.stacks == []):
            return True
        else:
            return False
        
    #returns everthing that is in the stack
	#But as a string 
    def __str__(self):
        return str(self.stacks)
"""
**********************
      Question 2
**********************
                    """
#Creates a new Stack called palindrome
#intializes variable newstring for checking words backwords
#pushes each letter of the string onto the stack
#Then pops eachletter into the newstring variable and out of the stack
#Therefore when it is its new string it has reversed it
#Checks to see if the newstring is the same as the old string
#returns true if so and false if not
def isPalindrome(string):
    palindrome = Stack()
    newstring = ''
    for x in range(0,len(string)):
        palindrome.push(string[x])
    for x  in range(len(string),0,-1):
        newstring = newstring + palindrome.pop()
    if(newstring == string):
        return True
    else:
        return False


"""
**********************
      Question 3
**********************
                    """
#This integer checks to see if the element in a string 
#is either an integer or a character
#if it is a number return True
#if not return false
def isInteger(string):
    for ch in string:
        if ch < '0' or ch > '9' : 
            return False
    return True;


#changes an integer to the string
#returns the string as an integer
def toInteger(string):
    return int(string)

#uses the stack that was created earlier
#use a for loop to check the string for integers and if there is one
#push that value as a integer into the stack
#if the value in the loop is not a number
#then it will pop the top 2 numbers and do string of what the operation is
#After the value is operated on the number is then pushed back onto the stack
#The function then will return the top of the stack
def calculateRPN(string):
    #Stack created
    RPN = Stack()
    #st is first num
    #nd is second num
    st = 0
    nd = 0
    #The number that is made from what is popped off
    newNum = 0
    for x in range(0, len(string)):
        if(isInteger(string[x])):
            RPN.push(toInteger(string[x]))
            
        else:
            if(string[x] == '+'):
                nd = RPN.pop()
                st = RPN.pop()
                #print(st, "+" , nd)
                newNum = st + nd
                RPN.push(newNum)

            elif(string[x] == '-'):
                nd = RPN.pop()
                st = RPN.pop()
                #print(st, "-" , nd)
                newNum = st - nd
                RPN.push(newNum)
                
            elif(string[x] == '*'):
                nd = RPN.pop()
                st = RPN.pop()
                #print(st, "*" , nd)
                newNum = st * nd
                RPN.push(newNum)
                
            elif(string[x]== '/'):
                nd = RPN.pop()
                st = RPN.pop()
                #print(st, "/" , nd)
                newNum = st / nd
                RPN.push(newNum)
                
                
    return RPN.top()
 
print(calculateRPN("5 7 1 1 + - / 3 * 2 1 1 + + -"))
