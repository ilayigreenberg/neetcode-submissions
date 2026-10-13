class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ('[', '(', '{'):
                stack.append(c)
            else:
                if not stack or not abs(ord(c) - ord(stack.pop())) < 3:
                    return False
        return False if stack else True