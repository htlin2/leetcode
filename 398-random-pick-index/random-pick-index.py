class Solution:

    def __init__(self, nums: List[int]):
        self.hashmap = collections.defaultdict(list)
        for i, n in enumerate(nums):
            self.hashmap[n].append(i)

    def pick(self, target: int) -> int:
        indices = self.hashmap[target]
        return random.choice(indices)
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

"""
key: count
1:1
2:1
3:3 33%
pick random from 1 ~ 3

"""