class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        adj = collections.defaultdict(set)
        for w in wordList:
            for i in range(len(w)):
                star_word = list(w)
                star_word[i] = '*'
                adj[''.join(star_word)].add(w)

        min_heap = [] # (count, word)
        heapq.heappush(min_heap, (0, beginWord))
        visited = set()
        while min_heap:
            count, w = heapq.heappop(min_heap)
            if w in visited: continue
            visited.add(w)
            count += 1
            if w == endWord: return count
            for j in range(len(w)):
                key = list(w)
                key[j] = '*'
                for nei in adj[''.join(key)]:
                    if nei in visited: continue
                    heapq.heappush(min_heap, (count, nei))
        return 0