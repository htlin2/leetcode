class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        left = 0
        res = 0
        visited = set() # char
        for right in range(N):
            # handle duplicate
            while s[right] in visited and left < right:
                # remove char in visited
                visited.remove(s[left])
                # move left pointer
                left += 1
            # handle not duplicate
            visited.add(s[right])
            res = max(len(visited), res)
        return res
"""
two pointers + hashmap
T: O(n)
S: O(n)
"""