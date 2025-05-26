class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {char: set() for word in words for char in word}
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            min_length = min(len(w1), len(w2))
            if w1[:min_length] == w2[:min_length] and len(w1) > len(w2):
                return ''
            for j in range(min_length):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        visited = set()
        cycle = set()
        res = []
        def has_cycle(char):
            if char in visited:
                return False
            if char in cycle:
                return True
            cycle.add(char)
            for nei in adj[char]:
                if has_cycle(nei):
                    return True
            visited.add(char)
            res.append(char)
            return False
        for k in adj.copy():
            if has_cycle(k):
                return ''
        return ''.join(res[::-1])
"""
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
w e r
    r t f
      t f
topcological sort
t: f
w: e
r: t
e: r

w -> e -> r -> t -> f
"""