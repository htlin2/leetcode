class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        digits = 0
        curr_sum = 0
        sign = 1
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
                curr_sum += (sign * digits)
                sign, digits = 1, 0
                prev_sum, prev_sign = stack.pop()
                curr_sum = prev_sum + (prev_sign * curr_sum)
        return curr_sum + sign * digits

"""
stack = [9]
time: O(n)
space: O(n)

-(3+(4+5))
stack = [(0, -), (3, +)]
res = 9
sign = 1
digits = 0
iterate through s:
    if char is digit:
        digits = digits * 10 + Number(char)
    if char is [+, -]:
        res += digits
        reset digits
        sign = -1
    if char == (:
        stack.push([res, sign])
        reset sign, res
    if char == ):
        res += sign * digits
        reset sign, digits
        const [prevRes, prevSign] = stack.pop()
        res = prevres + (prevSign * res)
return res + curr * sign
"""