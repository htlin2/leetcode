class Solution:
    def shortestDistance(self, words: List[str], w1: str, w2: str) -> int:
        w1_idx, w2_idx = -1, -1
        res = len(words)
        for i, w in enumerate(words):
            if w == w1:
                w1_idx = i
            elif w == w2:
                w2_idx = i

            if w1_idx != -1 and w2_idx != -1:
                res = min(res, abs(w1_idx - w2_idx))
        return res