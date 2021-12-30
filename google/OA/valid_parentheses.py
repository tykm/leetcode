class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        history = []
        for char in s:
            if char in ('(', '{', '['):
                history.append(char)
            else:
                if len(history) == 0:
                    return False
                else:
                    oppo = history.pop()
                    if char == ')' and oppo != '(':
                        return False
                    elif char == '}' and oppo != '{':
                        return False
                    elif char == ']' and oppo != '[':
                        return False
                
        return len(history) == 0
            