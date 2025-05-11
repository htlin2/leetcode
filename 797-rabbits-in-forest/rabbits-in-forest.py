class Solution:
    def numRabbits(self, ans: List[int]) -> int:
        res = 0
        counter = collections.Counter(ans)
        for num, freq in counter.items():
            group_size = num + 1
            groups = math.ceil(freq / group_size)
            res += groups * group_size
        return res