class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        adj = collections.defaultdict(set)
        for w in wordList:
            for i in range(len(w)):
                star_word = list(w)
                star_word[i] = '*'
                adj[''.join(star_word)].add(w)
        # print(adj)
        visited = set()
        min_heap = [[0, beginWord]]
        while min_heap:
            count, w = heapq.heappop(min_heap)
            if w in visited: continue
            visited.add(w)
            count += 1
            if w == endWord: return count
            for i in range(len(w)):
                star_word = list(w)
                star_word[i] = '*'
                for nei in adj[''.join(star_word)]:
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