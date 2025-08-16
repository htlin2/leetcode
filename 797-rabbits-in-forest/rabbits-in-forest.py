class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers = [a + 1 for a in answers]
        counter = collections.Counter(answers)
        res = 0
        for val, count in counter.items():
            if count <= val:
                res += val
            else:
                res += math.ceil(count / val) * val
        return res
"""
Input: answers = [1,1,2]
Output: 5

{
    2: 2
    3: 3
}
"""