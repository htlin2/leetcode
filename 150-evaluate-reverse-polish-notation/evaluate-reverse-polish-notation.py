class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator = set(['+', '-', '*', '/'])
        i = 0
        while i < len(tokens):
            if tokens[i] in operator:
                num1 = int(tokens[i - 2])
                num2 = int(tokens[i - 1])
                if tokens[i] == '+':
                    total = num1 + num2
                elif tokens[i] == '-':
                    total = num1 - num2
                elif tokens[i] == '*':
                    total = num1 * num2
                else:
                    total = int(num1 / num2)
                tokens = tokens[:i-2] + [total] + tokens[i+1:]
                i -= 2
            i += 1
        return int(tokens[0])