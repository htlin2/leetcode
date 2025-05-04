class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)
        count_words_tuples = sorted(counter.items(), key=lambda x: (-counter[x[0]], x[0]))[:k]
        return [tup[0] for tup in count_words_tuples]