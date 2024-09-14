class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        prefix = []
        curr_prefix = 1
        for n in nums:
            curr_prefix *= n
            prefix.append(curr_prefix)
        postfix = []
        curr_postfix = 1
        for i in range(N - 1, -1, -1):
            curr_postfix *= nums[i]
            postfix.append(curr_postfix)
        postfix.reverse()
        res = []
        for i in range(N):
            pre = prefix[i - 1] if i - 1 >= 0 else 1
            post = postfix[i + 1] if i + 1 < N else 1
            res.append(pre * post)
        return res

"""
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

prefix = [ 1, 2, 6,24]
postfix= [24,24,12, 4]
res    = [24,12, 8, 6] => prefix[i - 1] * postfix[i + 1]
Time: O(n)
Space: O(n)


Optimized
postfix= [24,12, 8, 4]
prefix  =           6
Time: O(n)
Space: O(1)
"""