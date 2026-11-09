class Solution:
    def evalRPN(self, tokens):
        ops = []
        c = tokens.pop()

        if c in ['+', '-', '*', '/']:
            ops.append(c)
        else: # if number
            if not ops:
                return c
            op = ops.pop()
            c1 = evalRPN(tokens)      
            return str(int(eval(c + op + c1)))
