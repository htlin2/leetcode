class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] # (char, count)
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][-1] += 1
            else:
                stack.append([char, 1])
            while stack and stack[-1][-1] >= k:
                stack[-1][-1] -= k
                if stack[-1][-1] == 0:
                    stack.pop()
                while len(stack) >= 2 and stack[-1][0] == stack[-2][0]:
                    char, count = stack.pop()
                    stack[-1][-1] += count
        res = ''
        for char, count in stack:
            res += char * count
        return res
"""
stack
Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"

"""