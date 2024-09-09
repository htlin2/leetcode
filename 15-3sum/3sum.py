class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        res = set()
        def two_sum(i, left, right):
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if three_sum == 0:
                    res.add((nums[i], nums[left], nums[right]))
                if three_sum <= 0:
                    left += 1
                else:
                    right -= 1
        for i in range(N - 2):
            two_sum(i, i + 1, N - 1)
        return list(res)


"""
1. for loop + hashmap + sort
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
[-4,-1,-1,-1,0,1,2]
     i     L     R  
-4 + -1 + 2 = -3 < 0, so L++
-4 +  0 + 2 = -2 < 0, so L++
-4 +  1 + 2 = -1 < 0, so L++

-1 + -1 + 2 = 0 <= 0, so L++  solution [-1,-1,2]
-1 +  0 + 2 = 1  > 0, so R--
-1 +  0 + 1 = 0 <= 0, so L++  solution [-1,0,1]
edge case:
    handle nums[i - 1] == nums[i], skip to next
    handle nums[L-1] == nums[L]
    or 
    make sure solutions are set
Time: O(n^2)
Space: O(n)

2. brute force
triple for loops
Time: O(n^3)
Space: O(n)
"""