import collections
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] # (char, count)
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][-1] += 1
            else:
                stack.append([char, 1])
            while stack and stack[-1][-1] == k:
                stack.pop()
        res = ''
        for char, count in stack:
            res += char * count
        return res
"""
Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"

stack + sliding window fixed

"""