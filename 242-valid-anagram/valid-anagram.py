class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        h = collections.defaultdict(int)
        for char in s:
            h[char] += 1
        for char in t:
            h[char] -= 1
            if h[char] < 0: return False
            if h[char] == 0: del h[char]
        return len(h) == 0
"""
1. brute force
for loops with s
pop char in t
Time: O(n^2)
Space: O(n)

2. hashmap
Time: O(n)
Space: O(n)

3. sort
Time: O(n log n)
Space: O(n)

"""