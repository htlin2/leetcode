class Solution:
    def numRabbits(self, ans: List[int]) -> int:
        res = 0
        counter = collections.Counter(ans)
        for key, val in counter.items():
            group = key + 1
            number = math.ceil(val / group)
            res += group * number
        return res