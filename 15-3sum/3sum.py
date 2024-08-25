class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        def two_sum(i, left, right):
            nonlocal res
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    res.add((nums[i], nums[left], nums[right]))
                if total <= 0:
                    left += 1
                else:
                    right -= 1
        N = len(nums)
        for i in range(N - 2):
            if i - 1 >= 0 and nums[i] == nums[i - 1]:
                continue
            two_sum(i, i + 1, N - 1)
        return list(res)


"""
for loop + 2 pointers
-1, -1, 2
-1 0 1
[-4,-1,-1,0,1,2]

def two_sum(i, left, right):
    while left < right:
        total = i + left + right
        if total == 0:
            append [i, left, right]
        if total <= 0:
            left += 1
        else:
            right -= 1
    
for loop:
    if i == prev_i:
        skip
    two_sum(i, i + 1, N - 1)

"""