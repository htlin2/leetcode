class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, res = 0, 0
        for n in nums:
            if count == 0:
                res = n
            if n == res:
                count += 1
            else:
                count -= 1
        return res

"""
count
nums = [2,2,1,1,1,2,2]
res  =  2 2 2 2 1 1 2
count=  1 2 1 0 1 0 1
"""