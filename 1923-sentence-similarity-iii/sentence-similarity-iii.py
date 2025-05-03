class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        q1 = collections.deque(s1.split(' '))
        q2 = collections.deque(s2.split(' '))
        while q1 and q2 and q1[0] == q2[0]:
            q1.popleft()
            q2.popleft()
        while q1 and q2 and q1[-1] == q2[-1]:
            q1.pop()
            q2.pop()
        return not q1 or not q2