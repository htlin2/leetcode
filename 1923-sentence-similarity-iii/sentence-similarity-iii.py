class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        s1_a, s2_a = s1.split(' '), s2.split(' ')
        q1, q2 = collections.deque(s1_a), collections.deque(s2_a)
        while q1 and q2 and q1[0] == q2[0]:
            q1.popleft()
            q2.popleft()
        while q1 and q2 and q1[-1] == q2[-1]:
            q1.pop()
            q2.pop()
        return True if not q1 or not q2 else False
"""
queue or stack?
"""