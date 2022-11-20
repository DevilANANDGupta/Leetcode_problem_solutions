class Solution:
    def calculate(self, ss: str) -> int:
        stack, acc, n, s = [], 0, 0, +1                  
        for c in filter(lambda ch: ch != " ", ss):        
            if c.isdigit() : n = 10*n + int(c)            
            if c in "+-"   : 
                acc += s*n                                
                n,s = 0, (c=="+")*2 - 1                   
            if c == "(":
                stack += (acc, s)                         
                acc, s = 0, +1                            
            if c == ")":
                acc += s*n                                
                acc = acc * stack.pop() + stack.pop()     
                n, s = 0, +1                              
        return acc + s*n                     
