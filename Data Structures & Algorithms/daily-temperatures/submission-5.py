class Solution:
    def dailyTemperatures(self, tempr):
        res = [0] * len(tempr)
        i = len(tempr) - 1
        stack = []
        while i >= 0:
            if stack and tempr[i] >= stack[-1][0]:
                stack.pop()
            else:
                if stack: res[i] = stack[-1][1] - i
                stack.append([tempr[i], i])
                i -= 1
        
        return res

