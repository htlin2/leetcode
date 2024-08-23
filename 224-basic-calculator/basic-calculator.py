class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res, curr = 0, 0
        sign = 1
        for char in s:
            if char.isdigit():
                curr = curr * 10 + int(char)
            elif char in ['+', '-']:
                res += curr * sign
                sign = 1 if char == '+' else -1
                curr = 0
            elif char == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif char == ')':
                res += curr * sign
                curr = 0
                stack_sign = stack.pop()
                res = stack.pop() + stack_sign * res
                sign = 1
        return res + curr * sign

"""
stack = []
temp = 1
prev_sign = +
-(1+(4+5+2)-3)+(6+8)
  1+   11  - 3 + 14

if digit:
    add to temp
elif sign:
    multiply temp with sign
( => append temp to stack, reset temp to 0, rest prev_sign = +
) => pop stacks and sum up


"""