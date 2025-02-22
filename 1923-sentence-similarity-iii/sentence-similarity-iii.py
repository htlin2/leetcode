class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        w1, w2 = s1.split(' '), s2.split(' ')
        q1, q2 = collections.deque(w1), collections.deque(w2)
        while q1 and q2 and q1[0] == q2[0]:
            q1.popleft()
            q2.popleft()
        while q1 and q2 and q1[-1] == q2[-1]:
            q1.pop()
            q2.pop()
        return len(q1) == 0 or len(q2) == 0
"""
queue
Input: 
sentence1 = "My name is Haley"
sentence2 = "My Haley"
w1 [name, is]
w2 []

"""