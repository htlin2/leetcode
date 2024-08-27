class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = s.split(' ')
        res = []
        for w in words:
            if not w: continue
            res.append(w)
        return ' '.join(res[::-1])