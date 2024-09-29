class Solution:
    def minInsertions(self, s: str) -> int:
        N = len(s)
        i, res = 0, 0
        stack = []
        while i < N:
            char = s[i]
            if char == '(':
                stack.append(char)
                i += 1
            elif char == ')':
                if i + 1 < N and s[i + 1] == ')':
                    if stack:
                        stack.pop()
                        i += 2
                    else:
                        res += 1
                        i += 2
                elif not stack:
                    res += 2
                    i += 1
                else:
                    stack.pop()
                    res += 1
                    i += 1
        return res + len(stack) * 2