class Solution:
    def candy(self, nums: List[int]) -> int:
        prefix = [1]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                prefix.append(prefix[i - 1] + 1)
            else:
                prefix.append(1)
        postfix = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                postfix[i] = postfix[i + 1] + 1
        combined = []
        for i in range(len(nums)):
            combined.append(max(prefix[i], postfix[i]))
        return sum(combined)
"""
prefix, postfix
Input: ratings = [1,0,2]
Output: 5

[ 1, 0, 2]
  1, 1, 2  prefix compare nums[i] and nums[i - 1]
  2  1  1  postifx compare nums[i] and nums[i + 1]

[ 1, 2, 2]
  1  2, 1  prefix
  1  1  1  postfix 
"""