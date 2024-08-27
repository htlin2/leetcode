class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        N = len(nums)
        counter = collections.defaultdict(int)
        max_f, left = 0, 0
        for right in range(N):
            counter[nums[right]] += 1
            max_f = max(max_f, counter[nums[right]])
            while (right - left + 1) - max_f > k:
                counter[nums[left]] -= 1
                left += 1
        return max_f

"""
Input: nums = [1,3,2,3,1,3], k = 3
output 3
0,1,2,3,4,5 - idx
1,3,2,3,1,3 - input
- 3 - 3 - 3
window = {1: 1, 3: 2, 2: 1, 4: 1}
1,3,2,3,4

[1,2,3,4,5] k = 1
 1 - 3 4 5
output 1

[1,1,2,2,1,1] k = 2
 1 1 - - 1 1 
 output 4  

[1] k = 100
output 1

1. hashmap
[1,3,2,3,1,3], k=3
{
    1: 2,
    2: 1,
    3: 3,
}
max is 3 that has count 3
min(k, N - 3)
Time: O(n)
Space: O(n)

2. brute force
[1,3,2,3,1,3], k=3
two for loops
[1,-,2,3,1,3], k=2
[1,-,-,-,1,3], k=0 -> output 2

[3,3,2,3,1,3], k=2
[3,3,3,3,1,3], k=1
[3,3,3,3,3,3], k=0 -> output 5
time: O(n^2)
time: O(1)
"""