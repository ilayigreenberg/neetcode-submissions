class Solution:
    def dailyTemperatures(self, tempr):
        res = [0] * len(tempr)
        stack = []  # will contain [val, indx]
        i = len(tempr) - 1
        while i > 0:
            if not stack or tempr[i] >= stack[-1][0]:
                stack.pop()
            else:
                res[i] = stack[-1][1] - i
                stack.append([tempr[i], i])
                i -= 1
        
        return res

