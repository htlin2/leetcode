class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            delta = target - n
            if delta in hashmap:
                return [hashmap[delta], i]
            hashmap[n] = i

"""
1. brute force
[11,15,2,7]
       i j     
11 + 15 = 26
11 + 2 = 13
11 + 7 = 18
2 + 7 = 9
Time: O(n^2)
Space: O(1)

2. hashmap
Input: nums = [11,15,2,7], target = 9
Output: [2,3]
hashmap = {  number: index
    11: 0,
    15: 1,
    2: 2

}
return [2,3]
time: O(n)
space: O(n)
"""