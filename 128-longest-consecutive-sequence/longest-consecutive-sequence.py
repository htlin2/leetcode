class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        hashmap = collections.defaultdict(int)
        for num in nums:
            if hashmap[num] != 0: continue
            prev_count = hashmap[num - 1]
            next_count = hashmap[num + 1]
            hashmap[num] = prev_count + next_count + 1
            hashmap[num - prev_count] = hashmap[num]
            hashmap[num + next_count] = hashmap[num]
        return max(hashmap.values())
"""
hashmap

"""