class Solution:
    def calculate(self, s: str) -> int:
        s = '+' + s.replace(' ', '') + '+'
        stack = []
        sign = ''
        num = 0
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            else:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] = stack[-1] * num
                elif sign == '/':
                    stack[-1] = int(stack[-1] / num)
                sign = char
                num = 0
        return sum(stack)