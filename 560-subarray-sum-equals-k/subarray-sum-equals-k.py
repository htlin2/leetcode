class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefix_sum = collections.defaultdict(int)
        prefix_sum[0] += 1
        curr_sum = 0
        for num in nums:
            curr_sum += num
            delta = curr_sum - k
            res += prefix_sum[delta]
            prefix_sum[curr_sum] += 1
        return res