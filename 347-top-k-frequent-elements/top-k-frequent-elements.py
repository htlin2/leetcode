class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        N = len(nums)
        freq = [[] for i in range(N + 1)]
        for key, val in counter.items():
            freq[val].append(key)
        res = []
        for i in range(len(freq) - 1, -1, -1):
            res = res + freq[i]
            if len(res) == k: return res
        return res
        