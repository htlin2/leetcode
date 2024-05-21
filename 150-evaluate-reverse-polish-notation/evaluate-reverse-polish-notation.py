class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = set(['+', '-', '*', '/'])
        # iterate through tokens:
        for t in tokens:
            if t not in operator:
                # append digit to stack
                stack.append(int(t))
                continue
            second = stack.pop()
            first = stack.pop()
            # handle each operator
            if t == '+':
                stack.append(first + second)
            elif t == '-':
                stack.append(first - second)
            elif t == '*':
                stack.append(first * second)
            else:
                stack.append(int(first / second))
        return stack[0]

"""
tokens = ["4","13","5","/","+"]
stack = []
Time: O(n)
Space: O(n)
"""