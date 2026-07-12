class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        sorted_tuples = sorted(counter.items(), key=lambda x: x[-1], reverse=True)
        res = []
        for key, value in sorted_tuples:
            res.append(key)
            if len(res) == k:
                return res
        return res