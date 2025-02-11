class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return self.areSentencesSimilar(s2, s1)
        w1, w2 = s1.split(' '), s2.split(' ')
        N1, N2 = len(w1), len(w2)
        l1, l2 = 0, 0
        while l1 < N1 and l2 < N2 and w1[l1] == w2[l2]:
            l1 += 1
            l2 += 1
        r1, r2 = N1 - 1, N2 - 1
        while r1 >= 0 and r2 >= 0 and w1[r1] == w2[r2]:
            r1 -= 1
            r2 -= 1
        return l1 > r1