class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        res = 0
        i = 0
        while i < len(s):
            if s[i] == '(':
                stack.append(s[i])
                i += 1
            else:
                # )
                if i + 1 < len(s) and s[i + 1] == ')':
                    if stack:
                        stack.pop()
                    else:
                        res += 1
                    i += 2
                else:
                    if stack:
                        stack.pop()
                        res += 1
                        i += 1
                    else:
                        res += 2
                        i += 1
        return res + len(stack) * 2