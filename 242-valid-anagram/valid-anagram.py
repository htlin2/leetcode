class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        hashmap = collections.defaultdict(int)
        for char in s:
            hashmap[char] += 1
        for char in t:
            if char not in hashmap: return False
            hashmap[char] -= 1
            if hashmap[char] < 0: return False
        return True