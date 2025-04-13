class Solution:
    def minInsertions(self, s: str) -> int:
        inserts = 0
        stack = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                stack.append(s[i])
                i += 1
            else:
                # s[i] == ')'
                if i + 1 < len(s) and s[i + 1] == ')':
                    if stack:
                        stack.pop()
                    else:
                        inserts += 1
                    i += 2
                else:
                    if stack:
                        stack.pop()
                        inserts += 1
                        i += 1
                    else:
                        inserts += 2
                        i += 1
        return inserts + len(stack) * 2