class Solution:
    def evalRPN(self, tokens):

        op = tokens.pop()
        oprd1 = tokens[0]
        if tokens[-1] in ["+","-","*","/"]:
            oprd2 = self.evalRPN(tokens[1:])
        return int(eval(oprd1 + op + oprd2))
        