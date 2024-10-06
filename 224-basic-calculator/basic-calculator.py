class Solution:
    def calculate(self, s: str) -> int:
        stack = [] # (curr_sum, sign)
        sign, digits, curr_sum = 1, 0, 0
        for char in s:
            if char.isdigit():
                digits = digits * 10 + int(char)
            elif char in '+-':
                curr_sum += sign * digits
                sign = 1 if char == '+' else -1
                digits = 0
            elif char == '(':
                stack.append((curr_sum, sign))
                curr_sum, sign = 0, 1
            elif char == ')':
                curr_sum += sign * digits
                sign, digits = 1, 0
                prev_sum, prev_sign = stack.pop()
                curr_sum = prev_sum + prev_sign * curr_sum
        return curr_sum + sign * digits
"""
stack
Example 2:
Input: s = "2-1+2"
Output: 3
stack = [3]
sign   = + 
digits = 2
starts with sign = +, stack = [0], digits = 0
if num, add to digits
if sign, add stack[-1] + digits, reset digits to 0, assign sign with sign
add remaining digits stack
sum up all stack as result


Example 3:
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
stack  = [0, 12] sign, num
sign   = -
digits = 3
what to do with parentheses?
"""