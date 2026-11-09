class Solution:
    def evalRPN(self, tokens):
        ops = []
        while tokens:
            c = tokens.pop()

            if c in ['+', '-', '*', '/']:
                ops.append(c)
            else: # if number
                if not ops:
                    return int(c)
                op = ops.pop()
                while True:
                    c1 = self.evalRPN(tokens)      
                    res = int(eval(str(c1) + op + str(c)))
                    if not ops:
                        return res
                    c = res
