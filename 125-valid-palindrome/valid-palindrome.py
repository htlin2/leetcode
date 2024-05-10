class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''
        for char in s:
            if char.isalnum():
                new_s += char.lower()
        return new_s == new_s[::-1]

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