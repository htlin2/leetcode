class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = collections.defaultdict(int)
        res = 0
        for n in nums:
            if hashmap[n] != 0: continue
            prev_num = n - 1
            next_num = n + 1
            hashmap[n] = hashmap[prev_num] + hashmap[next_num] + 1
            hashmap[n - hashmap[prev_num]] = hashmap[n]
            hashmap[n + hashmap[next_num]] = hashmap[n]
            res = max(res, hashmap[n])
        return res