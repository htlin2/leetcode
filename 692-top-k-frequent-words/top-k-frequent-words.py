class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)
        count_words = collections.defaultdict(list)
        for word, count in counter.items():
            count_words[count].append(word)
        for values in count_words.values():
            values.sort()
        count_words_tuples = sorted(count_words.items(), reverse=True, key=lambda x: x[0])
        res = []
        for _count, words in count_words_tuples:
            res += words
        return res[:k]