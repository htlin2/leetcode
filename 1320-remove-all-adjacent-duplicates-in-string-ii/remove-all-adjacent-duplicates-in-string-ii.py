class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] # (char, count)
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][-1] += 1
                if stack[-1][-1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])
        res = ''
        for char, count in stack:
            res += char * count
        return res

"""
stack
Example 2:

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
deeedbbcccbdaa
a: 2


Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"
stack
p:1 , s
"""