class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(left, right):
            while left <= right:
                if left == right: return True
                if s[left] != s[right]: return False
                left += 1
                right -= 1
            return True
        N = len(s)
        left, right = 0, N - 1
        while left <= right:
            if left == right: return True
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
        return True


"""
what is palindrome?
abc => no
abca => yes
aba => yes

abba => yes
'' => yes
cabba => yes

1. two pointers
cabba
l   r
 l  r 
  lr

ab ca
l   r
 l r
 lr
l++ or r--

"""