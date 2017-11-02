""" palindrome checker """
def palichecker(word):
    p=''
    d=[]
    for char in range(len(word)):
        d.push(word[char])
    for x in range(len(word)):
      p=p+d.pop
    if(p==word): return True
    return False
print (palichecker('tacocat'))
