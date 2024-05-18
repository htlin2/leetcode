class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine): return False
        ransom_hashmap = collections.Counter(ransomNote)
        for m in magazine:
            if m in ransom_hashmap:
                ransom_hashmap[m] -= 1
                if ransom_hashmap[m] == 0:
                    del ransom_hashmap[m]
            if not ransom_hashmap: return True
        return False
"""
1. hashmap
ransomNote_hashmap
iterate through magazine
    decrement ransomNote_hashmap's value
    if ransomNote_hashmap is empty: return True
return False
Time: O(n + m) or O(max(n, m))
Space: O(n)

2. brute force
iterate through ransomNote:
    pop the charactor in magazine
    if can't pop, return False
return True
Time: O(n * m^2)
Space: O(1)
"""