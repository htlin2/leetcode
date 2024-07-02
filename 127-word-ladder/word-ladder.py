class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        adj = collections.defaultdict(set) # word: [word1, word2]
        for w in wordList:
            for i in range(len(w)):
                key = list(w)
                key[i] = '*'
                adj[''.join(key)].add(w)

        visited = set()
        min_heap = [[0, beginWord]]
        while min_heap:
            count, w = heapq.heappop(min_heap)
            visited.add(w)
            count += 1
            if w == endWord: return count
            for i in range(len(w)):
                key = list(w)
                key[i] = '*'
                for nei in adj[''.join(key)]:
                    if nei in visited: continue
                    heapq.heappush(min_heap, [count, nei])
        return 0


"""
hashmap + graph (bfs)
Input: beginWord = "hit", endWord = "cog"
["hot","dot","dog","lot","log","cog"]
hit > hot > dot > dog > cog

build adj
*it = []
h*t = [hot]
hi* = []

*ot = [dot, lot]
h*t = []
ho* = []

*ot = []
d*t
do* = [dog]

*og = [cog]

"""