class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    ans.append((nums[i], nums[l], nums[r]))
                    l, r = l + 1, r - 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return set(ans)
"""
1. for loop + two pointers
sort input array
[-4, -1, -1,0,1,2]
for loop
    two pointers
    if sum is 0: append to result
    if sum is < 0:
        increment left
    else:
        decrement right
Time: O(n log n)
space: O(n)

2. brute force
3 for loops
time: O(n ^ 3)
space: O(1)
"""