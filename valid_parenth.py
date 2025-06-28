class Solution(object):
    def isValid(self, s):
        stack = []

        for char in s:
            if char == '(':          
                stack.append(char)   
            elif char == ')':        
                if not stack:        
                    return False
                stack.pop()          

        return len(stack) == 0 

# 28th June, 2025, Saturday, 9:45pm
        
