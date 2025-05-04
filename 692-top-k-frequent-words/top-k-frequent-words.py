class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)
        max_heap = [(-count, word) for word, count in counter.items()]
        heapq.heapify(max_heap)
        res = []
        while k:
            _count, word = heapq.heappop(max_heap)
            res.append(word)
            k -= 1
        return res