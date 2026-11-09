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
                c1 = evalRPN(tokens)      
                return int(eval(str(c) + op + str(c1)))
