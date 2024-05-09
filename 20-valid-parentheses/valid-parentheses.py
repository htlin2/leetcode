class Solution:
    def isValid(self, s: str) -> bool:
        h = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for char in s:
            if char in h:
                stack.append(h[char])
                continue
            if not stack or stack[-1] != char: return False
            stack.pop()
        return len(stack) == 0
"""
1) stack
stack = (
Time: O(n)
Space: O(n)

"""