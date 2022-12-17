import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        if len(tokens) == 1: return int(tokens[0])
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                second_operand = stack.pop()
                first_operand = stack.pop()
                tmp=0
                if token == '+':
                    tmp = first_operand + second_operand
                elif token == '-':
                    tmp = first_operand - second_operand
                elif token == '*':
                    tmp = first_operand * ssecond_operand
                elif token == '/':
                    tmp = first_operand / second_operand
                    tmp = math.trunc(tmp)
                stack.append(tmp)
        return stack.pop()
