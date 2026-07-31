class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in ['+', '-', '*', '/']:
                stack.append(int(t))
            else:
                prev = stack.pop()
                if t == '+':
                    stack[-1] += prev
                elif t == '-':
                    stack[-1] -= prev
                elif t == '*':
                    stack[-1] *= prev
                elif t == '/':
                    prev_prev = stack[-1]
                    stack[-1] = int(prev_prev / prev)
        return stack[0]
"""
stack

"""