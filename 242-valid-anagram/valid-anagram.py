class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = collections.Counter(s)
        t = collections.Counter(t)
        return s == t