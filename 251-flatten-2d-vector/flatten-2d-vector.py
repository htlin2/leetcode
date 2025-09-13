class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.q = collections.deque(self.flat(vec))
        
    def flat(self, arr):
        res = []
        for a in arr:
            if isinstance(a, list):
                res += self.flat(a)
            else:
                res.append(a)
        return res

    def next(self) -> int:
        return self.q.popleft()

    def hasNext(self) -> bool:
        return True if self.q else False


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()