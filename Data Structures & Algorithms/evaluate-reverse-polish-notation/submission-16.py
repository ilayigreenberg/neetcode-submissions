class Solution:
    
    def evalRPN(self, tokens):
        import operator
        op_map = {
            "+" : operator.add,
            "-" : operator.sub,
            "*" : operator.mul,
            "/" : operator.truediv
        }

        ops = []
        while tokens:
            c = tokens.pop()

            if c in ['+', '-', '*', '/']:
                ops.append(c)
            else: # if number
                if not ops:
                    return int(c)
                while True:
                    c1 = self.evalRPN(tokens)      
                    op = ops.pop()
                    res = int(op_map[op](c1, int(c)))
                    if not ops:
                        return res
                    c = res

#time O(N)  space: O(N) - recursion