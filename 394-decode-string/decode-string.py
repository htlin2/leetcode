class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != ']':
                stack.append(char)
                continue
            digits, letters = '', ''
            while stack and stack[-1].isalpha():
                letters = stack.pop() + letters
            stack.pop()
            while stack and stack[-1].isdigit():
                digits = stack.pop() + digits
            substr = int(digits) * letters
            stack.append(substr)
        return ''.join(stack)