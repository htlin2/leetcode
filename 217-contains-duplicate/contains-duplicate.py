class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = collections.Counter(nums)
        for k, v in counter.items():
            if v >= 2: return True
        return False

"""
1) sort nums
for loop to check if neighbor has dupicate
time: O(n log n)
space: O(n)

2) hashmap
time: O(n)
space: O(n)

3) brute force
time: O(n^2)
space: O(1)
"""