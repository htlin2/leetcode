class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1
        while L < R:
            while L < R and not (s[L].isalpha() or s[L].isdigit()):
                L += 1
            while L < R and not s[R].isalnum():
                R -= 1
            if s[L].lower() != s[R].lower(): return False
            L, R = L + 1, R - 1
        return True

"""
1) brute force
clean up s - remove space, make lower case
reverse s
compare reversed_s == s
Time: O(n)
Space: O(n)

2) two pointers
while L <= R:
    if L == R: return True
    if s[L] is not alpha, increment L++
    if s[R] is not alpha, decrement R--
    if s[L] != s[R]: return False
    L++
    R--
return True
Time: O(n)
Space: O(1)
"""