class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            match token:
                case '+':
                    x = stack.pop()
                    y = stack.pop()
                    stack.append(x + y)
                case '-':
                    x = stack.pop()
                    y = stack.pop()
                    stack.append(y - x)

                case '*':
                    x = stack.pop()
                    y = stack.pop()
                    stack.append(x * y)
                
                case '/':
                    x = stack.pop()
                    y = stack.pop()
                    stack.append(int(y/x))
                
                case _:
                    stack.append(int(token))

        return stack[0]
                

