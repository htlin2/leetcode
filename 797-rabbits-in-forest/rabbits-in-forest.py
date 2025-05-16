class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # answers = [a + 1 for a in answers]
        counter = collections.Counter(answers)
        res = 0
        for k, v in counter.items():
            group_size = k + 1
            number = math.ceil(v / group_size)
            res += group_size * number
        return res