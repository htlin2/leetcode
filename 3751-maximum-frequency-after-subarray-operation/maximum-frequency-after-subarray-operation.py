class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        counter = collections.Counter(nums)
        max_increase = 0
        for t in range(1, 51):
            if t == k: continue
            curr_sum = max_sum = 0
            for num in nums:
                if num == t:
                    curr_sum += 1
                elif num == k:
                    curr_sum -= 1
                curr_sum = max(curr_sum, 0)
                max_sum = max(max_sum, curr_sum)
            max_increase = max(max_increase, max_sum)
        return counter.get(k, 0) + max_increase