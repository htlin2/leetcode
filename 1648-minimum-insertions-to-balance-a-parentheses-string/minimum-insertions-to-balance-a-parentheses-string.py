class Solution:
    def minInsertions(self, s: str) -> int:
        res = 0
        stack = [] # (
        i = 0
        while i < len(s):
            char = s[i]
            if char == '(':
                stack.append(char)
                i += 1
            elif char == ')':
                if i + 1 < len(s) and s[i + 1] == ')':
                    if stack:
                        stack.pop()
                        i += 2
                    else:
                        i += 2
                        res += 1
                else:
                    # only single )
                    if stack:
                        stack.pop()
                        i += 1
                        res += 1
                    else:
                        i += 1
                        res += 2
        return res + len(stack) * 2
                