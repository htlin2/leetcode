class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        hashmap = collections.defaultdict(int)
        for key, weight in items1:
            hashmap[key] += weight

        for key, weight in items2:
            hashmap[key] += weight
        res = []
        for key in sorted(hashmap.keys()):
            res.append([key, hashmap[key]])
        return res