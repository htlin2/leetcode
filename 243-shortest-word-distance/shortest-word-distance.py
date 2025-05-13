class Solution:
    def shortestDistance(self, words: List[str], w1: str, w2: str) -> int:
        w1_idx, w2_idx = [], []
        for i, w in enumerate(words):
            if w == w1:
                w1_idx.append(i)
            elif w == w2:
                w2_idx.append(i)
        res = float('inf')
        for i in w1_idx:
            for j in w2_idx:
                delta = abs(i - j)
                res = min(res, delta)
        return res
"""
tri?
"""