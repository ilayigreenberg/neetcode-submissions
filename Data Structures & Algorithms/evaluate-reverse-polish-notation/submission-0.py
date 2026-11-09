class Solution:
    def evalRPN(self, tokens):
        oprd1, oprd2, op = tokens[0], tokens[1], tokens[2]
        res = int(eval(oprd1 + op + oprd2))
        for i in range(3, len(tokens) - 1):
            oprd2, op = tokens[i], tokens[i + 1]
            oprd1 = str(res)
            res = int(eval(oprd1 + op + oprd2))
        return res

            
