class Solution:
    def rob(self, nums: List[int]) -> int:
        rob, skip = 0, 0
        for i in range(len(nums) - 1, -1, -1):
            temp = max(skip + nums[i], rob)
            # skip
            skip = rob
            # rob
            rob = temp
        return rob