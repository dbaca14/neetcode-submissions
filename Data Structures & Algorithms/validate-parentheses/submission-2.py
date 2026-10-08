class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Map closing brackets to their corresponding opening brackets
        mapping = {")": "(", "]": "[", "}": "{"}
        
        for char in s:
            if char in mapping:
                # Get the top element of the stack if it's not empty, else use a dummy value
                top_element = stack.pop() if stack else '#'
                
                # If the mapping for this closing bracket doesn't match the stack's top
                if mapping[char] != top_element:
                    return False
            else:
                # It is an opening bracket, push it onto the stack
                stack.append(char)
        
        # If the stack is empty, all opening brackets were matched
        return not stack
