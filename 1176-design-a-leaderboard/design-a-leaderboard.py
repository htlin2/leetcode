class Leaderboard:

    def __init__(self):
        self.cache = collections.defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.cache[playerId] += score

    def top(self, K: int) -> int:
        scores = []
        for score in self.cache.values():
            heapq.heappush(scores, score)
            if len(scores) > K:
                heapq.heappop(scores)
        res = sum(scores)
        return abs(res)

    def reset(self, playerId: int) -> None:
        self.cache[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)