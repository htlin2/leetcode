class Solution:
    def decodeString(self, s: str) -> str:
        stack = [] # (chars, count)
        digits, chars = 0, ''
        for char in s:
            if char.isdigit():
                digits = digits * 10 + int(char)
            elif char.isalpha():
                chars += char
            elif char == '[':
                stack.append((chars, digits))
                chars, digits = '', 0
            elif char == ']':
                stack_chars, stack_count = stack.pop()
                chars = stack_chars + stack_count * chars
        return chars
"""
stack 
Input: s = "3[a]2[bc]"
Output: "aaabcbc"
stack = [(aaa, 2)] # (characters, count)
digits = 0
characters = aaabcbc
3[a]2[bc]
        i


Input: s = "3[a2[c]]"
Output: "accaccacc"
stack = [('', 3) ] # (characters, count)
digits = 0
chars = '' + accaccacc
3[a2[c]]
       i 
if digit:
    add to digits
elif char:
    add to characters
elif [:
    stack.append((characters, digits))
    reset characters, digits
elif ]:
    stack_char, stack_digits = pop stack
    chars = stack_char + stack_digits * chars
"""