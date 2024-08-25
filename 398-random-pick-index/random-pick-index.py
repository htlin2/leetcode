class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.hashmap = collections.defaultdict(int)
        for n in nums:
            self.hashmap[n] += 1

    def pick(self, target: int) -> int:
        count = self.hashmap[target]
        pick = random.randrange(1, count + 1)
        curr_count = 0
        for i, n in enumerate(self.nums):
            if n == target:
                curr_count += 1
            if curr_count == pick:
                return i
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