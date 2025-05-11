class Solution:
    def numRabbits(self, ans: List[int]) -> int:
        res = 0
        counter = collections.Counter(ans)
        for num, count in counter.items():
            group_size = num + 1
            groups = math.ceil(count / group_size)
            res += groups * group_size
        return res