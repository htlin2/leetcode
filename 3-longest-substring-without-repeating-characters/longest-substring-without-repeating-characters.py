class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        window = collections.defaultdict(int)
        l = 0
        for r in range(len(s)):
            window[s[r]] += 1
            while window[s[r]] > 1 and l < r:
                window[s[l]] -= 1
                l += 1
            max_length = max(max_length, r - l + 1)
        return max_length
"""
1) sliding window variable
Input: s = "p w w k e w"
                  l    r
Output: 3
window = {w: 1, k: 1, e:1}
ans = 3

time: O(n)
space: O(26) -> O(1)

2) brute force
two for loops + hashmap
time: O(n^ 2)
space: O(26) -> O(1)
"""