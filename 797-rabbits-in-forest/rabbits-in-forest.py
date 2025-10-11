class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = collections.Counter([a + 1 for a in answers])
        res = 0
        for key, count in counter.items():
            number = count // key
            plus_one = 1 if count % key >= 1 else 0
            number += plus_one
            res += number * key
        return res
"""
counter
"""