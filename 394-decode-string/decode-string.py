class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ']':
                substr, digits = '', ''
                while stack and stack[-1] != '[':
                    substr = stack.pop() + substr
                stack.pop() # pop [
                while stack and stack[-1].isdigit():
                    digits = stack.pop() + digits
                stack.append(int(digits) * substr)
            else:
                stack.append(char)
        return ''.join(stack)
