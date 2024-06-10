class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = collections.Counter(s)
        t_counter = collections.Counter(t)
        return s_counter == t_counter