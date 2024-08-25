class Leaderboard:

    def __init__(self):
        self.player_score = {}

    def addScore(self, playerId: int, score: int) -> None:
        if not playerId in self.player_score:
            self.player_score[playerId] = 0
        self.player_score[playerId] += score

    def top(self, K: int) -> int:
        scores = self.player_score.values()
        sorted_scores = sorted(scores)[::-1]
        top_k = sorted_scores[:K]
        return sum(top_k)


    def reset(self, playerId: int) -> None:
        del self.player_score[playerId]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)


# hashset + max_heap
# hashset to track players that rest score
# max_heap to get top k

"""
["Leaderboard","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","addScore","top","reset","reset","addScore","reset"]

"""