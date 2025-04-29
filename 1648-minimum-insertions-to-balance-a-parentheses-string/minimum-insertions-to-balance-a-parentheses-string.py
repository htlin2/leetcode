class Solution:
    def minInsertions(self, s: str) -> int:
        res = 0
        stack = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                stack.append(s[i])
                i += 1
            else:
                # ')'
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
        res += len(stack) * 2
        return res