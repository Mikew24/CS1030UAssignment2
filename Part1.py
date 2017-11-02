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
        if(self.stacks == []):
            return True
        else:
            return False
        
        
    def __str__(self):
        return str(self.stacks)
