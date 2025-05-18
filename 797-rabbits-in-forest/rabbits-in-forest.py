class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers = [a + 1 for a in answers]
        counter = collections.Counter(answers)
        res = 0
        for group_size, count in counter.items():
            number = math.ceil(count / group_size)
            res += number * group_size
        return res