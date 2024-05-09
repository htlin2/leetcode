class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {} # {num: index}
        for i, n in enumerate(nums):
            delta = target - n
            if delta in h:
                return [h[delta], i]
            h[n] = i
"""
1) brute force
Time: O(n^2)
Space: O(1)

2) hashmap = {num: index}
Time: O(n)
Space: O(n)

3) two pointers + sort
(num, index)
[(2,1), (3,0), (4, 2)]
Time: O(n log n)
Space: O(n)
"""