class Solution:
    def decodeString(self, s: str) -> str:
        stack = [] # (substr, digits)
        substr, digits = '', 0
        for char in s:
            if char.isdigit():
                digits = digits * 10 + int(char)
            elif char.isalpha():
                substr += char
            elif char == '[':
                stack.append((substr, digits))
                substr, digits = '', 0
            elif char == ']':
                s_substr, s_digits = stack.pop()
                substr = s_substr + s_digits * substr
        return substr

"""
Input: s = "3[a]2[bc]"
Output: "aaabcbc"
stack = [(aaa, 2)]
digits = 0
substr = bc


Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"
stack = [('', 3)]
digits = 0
substr = ''  + accaccacc
loop through s:
    if char is digit:
        add to digits
    elif char is alphbets:
        add to substr
    elif char == [:
        append (substr, digits) to stack
        reset substr, digits
    elif char == ]:
        stack_char, stack_digits = stack.pop()
        substr = stack_char + substr * stack_digits
        add substr to res
"""