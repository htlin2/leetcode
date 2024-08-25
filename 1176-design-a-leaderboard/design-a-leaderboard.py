class Leaderboard:

    def __init__(self):
        self.cache = collections.defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.cache[playerId] += score

    def top(self, K: int) -> int:
        scores = [ -v for v in self.cache.values()]
        heapq.heapify(scores)
        res = 0
        while K:
            res += heapq.heappop(scores)
            K -= 1
        return abs(res)

    def reset(self, playerId: int) -> None:
        self.cache[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)