class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        adj = collections.defaultdict(set)
        for word in wordList:
            for i in range(len(word)):
                star_word = word[:i] + '*' + word[i+1:]
                adj[star_word].add(word)
        visited = set()
        res = 0
        q = collections.deque([beginWord])
        while q:
            res += 1
            for _ in range(len(q)):
                first = q.popleft()
                if first in visited: continue
                visited.add(first)
                if first == endWord:
                    return res
                for i in range(len(first)):
                    star_word = first[:i] + '*' + first[i+1:]
                    for nei in adj[star_word]:
                        q.append(nei)
        return 0
"""
BFS + hashmap
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5 
"hit" -> "hot" -> "dot" -> "dog" -> cog"
ho*: hot
h*t: hot
*ot: hot, dot, lot
do*: dot, dog
d*t: dot
d*g: dog
*og: dog, log, cog

visited = hot
count = 3
q = [dot, lot]

{
    '*ot': {'dot', 'hot', 'lot'}, 
    'h*t': {'hot'}, 
    'ho*': {'hot'}, 
    'd*t': {'dot'}, 
    'do*': {'dot', 'dog'}, 
    '*og': {'log', 'cog', 'dog'}, 
    'd*g': {'dog'}, 
    'l*t': {'lot'}, 
    'lo*': {'log', 'lot'}, 
    'l*g': {'log'}, 
    'c*g': {'cog'}, 
    'co*': {'cog'}
}
"""