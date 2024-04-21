class AuthenticationManager:
    def __init__(self, ttl: int):
        self.ttl = ttl
        self.id_expired_map = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.id_expired_map[tokenId] = currentTime + self.ttl

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.id_expired_map: return
        # the expiration takes place before the other actions
        if self.id_expired_map[tokenId] <= currentTime: return
        self.generate(tokenId, currentTime)

    def countUnexpiredTokens(self, currentTime: int) -> int:
        exp_times = self.id_expired_map.values()
        count = 0
        for t in exp_times:
            if t <= currentTime: continue
            count += 1
        return count


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)