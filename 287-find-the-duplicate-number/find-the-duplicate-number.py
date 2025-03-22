class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        N = len(nums)
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow2 == slow:
                return slow
"""
[ 1, 3, 4, 2, 2]
  0, 1, 2, 3, 4
0 -> 1 -> 3 -> 2 -> 4
                 <-
sf  sf   sf   sf     sf

ex 2:
output 3
[ 3, 1, 3, 4, 2]
  0, 1, 2, 3, 4
0 -> 3 -> 4 -> 2
     3  <----  2
              sf 
"""