class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) < 3:
            return int(tokens[0])
        stack = []
        for i in tokens:
            if i == '+':
                y = stack.pop()
                x = stack.pop()

                add = int(x) + int(y)
                stack.append(add)
            elif i == '-':
                y = stack.pop()
                x = stack.pop()

                diff = int(x) - int(y)
                stack.append(diff)
            elif i == '*':
                x = stack.pop()
                y = stack.pop()

                prod = int(x) * int(y)
                stack.append(prod)
            elif i == '/':
                y = stack.pop()
                x = stack.pop()

                quot = int(x) / int(y)
                stack.append(quot)
            else:
                stack.append(i)
            
        return int(stack.pop())