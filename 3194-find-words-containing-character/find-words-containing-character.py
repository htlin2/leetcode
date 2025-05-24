class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = set()
        for i, w in enumerate(words):
            if x in w:
                res.add(i)
        return list(res)