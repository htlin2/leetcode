class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        nums = [a + 1 for a in answers]
        counter = collections.Counter(nums)
        res = 0
        for group_size, group_count in counter.items():
            num = math.ceil(group_count / group_size)
            res += group_size * num
        return res