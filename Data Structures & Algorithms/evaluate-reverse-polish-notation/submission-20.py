class Solution:
    def evalRPN(self, tokens):
        import operator
        op_map = {
            "+" : operator.add,
            "-" : operator.sub,
            "*" : operator.mul,
            "/" : lambda x,y : int(x / y)
        }

        stack, ops= [], ['+', '-', '*', '/']
        while tokens:
            c = tokens.pop()
            if c in ops:
                stack.append(c)
            else: # if number
                if not tokens:
                    return op_map[stack.pop()](int(c1), int(c))
                if tokens[-1] in ops:
                    stack.append(c)
                else:
                    while c not in ops:
                        c1 = tokens.pop()
                        while c not in ops:
                            c1 = op_map[stack.pop()](int(c1), int(c))
                            if not stack:
                                return c1
                            c = stack.pop()
                        stack.append(c)
                        c = c1









