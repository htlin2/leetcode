class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        substr, digits = '', ''
        for char in s:
            if char == ']':
                while stack and stack[-1] != '[':
                    substr = stack.pop() + substr
                stack.pop() # pop [
                while stack and stack[-1].isdigit():
                    digits = stack.pop() + digits
                stack.append(int(digits) * substr)
                substr, digits = '', ''
            else:
                stack.append(char)
        stack.append(substr)
        return ''.join(stack)

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