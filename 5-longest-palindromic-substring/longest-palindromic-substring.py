class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        res = ''
        def get_palindrome(left, right):
            if s[left] != s[right]: return ''
            while 0 <= left and right < N and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1: right]
        for i in range(N):
            odd = get_palindrome(i, i)
            even = get_palindrome(i, i + 1) if i + 1 < N else ''
            if len(odd) > len(res):
                res = odd
            if len(even) > len(res):
                res = even
        return res
"""
dp - odd even
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
 b a b a d
odd = b -> o
even  ba -> x
     aba -> o
    babad -> x



babab



"""