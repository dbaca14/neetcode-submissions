class Solution:
    def isValid(self, s: str) -> bool: 
        openBraces = { "}": "{", "]": "[" ,")": "(" } 
        stack = [] 
        for bracket in s: 
            if bracket in openBraces: 
                if not stack: 
                    return False 
                top = stack.pop() 
                if top != openBraces[bracket]: 
                    return False 
            else: 
                stack.append(bracket) 
        if stack: 
            return False 
        else: 
            return True
