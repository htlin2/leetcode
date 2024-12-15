class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        def get_palindrome(left, right):
            ans = ''
            while left >= 0 and right < N:
                if s[left] == s[right]:
                    ans = s[left:right + 1]
                else:
                    return ans
                left -= 1
                right += 1
            return ans
        res = ''
        for i in range(N):
            left = i
            right = i + 1 if i + 1 < N else i
            # check odd
            odd = get_palindrome(left, left)
            if odd and len(res) <= len(odd):
                res = odd
            # check even
            even = get_palindrome(left, right)
            if even and len(res) <= len(even):
                res = even
        return res