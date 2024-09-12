class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        window = collections.defaultdict(int)
        left, max_f = 0, 0
        for right in range(len(nums)):
            window[nums[right]] += 1
            max_f = max(max_f, window[nums[right]])
            while (right - left + 1) - max_f > k:
                window[nums[left]] -= 1
                left += 1
        return max_f


"""
Input: nums = 
[1,3,2,3,1,3], k = 3
[1,3,_,3,_,3], k = 3

counter {
    1: 1
    3: 2
    2: 1
}

1, 2, 3
delete or skip
delet k -= 1
backtracking + memo
dfs(i, k, prev_num):
    prev_num


[1,3,_,3,_,3], k = 3
max_freq = 1
"""
