class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap_s1 = collections.Counter(s1)
        for i in range(len(s2)):
            char = s2[i]
            if not char in hashmap_s1:
                continue
            substring_s2 = s2[i:i+len(s1)]
            hashmap_s2 = collections.Counter(substring_s2)
            if hashmap_s1 == hashmap_s2:
                return True
        return False
"""
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

hashmap_s1 = {a: 1, b: 1}

"""