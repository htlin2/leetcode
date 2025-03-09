class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = collections.defaultdict(int)
        res = 0
        for n in nums:
            if hashmap[n] != 0: continue
            prev_val = hashmap[n - 1]
            next_val = hashmap[n + 1]
            hashmap[n] = prev_val + next_val + 1
            hashmap[n - prev_val] = hashmap[n]
            hashmap[n + next_val] = hashmap[n]
            res = max(res, hashmap[n])
        return res