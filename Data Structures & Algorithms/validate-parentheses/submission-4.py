class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if s == '':
            return False

        for e in s:
            if e in '({[':
                stack.append(e)
            else:
                if stack and (e == ']' and stack[-1] == '['
                 or e == '}' and stack[-1] == '{' or e == ')' and stack[-1] == '('):
                 stack.pop() 
                else:
                    return False

        return len(stack) == 0