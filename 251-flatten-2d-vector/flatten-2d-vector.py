class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.q = collections.deque(self.flatten(vec))

    def flatten(self, arr):
        res = []
        for int_or_arr in arr:
            if isinstance(int_or_arr, list):
                curr = self.flatten(int_or_arr)
                res = [*res, *curr]
            elif isinstance(int_or_arr, int):
                res.append(int_or_arr)
        return res

    def next(self) -> int:
        return self.q.popleft()

    def hasNext(self) -> bool:
        return len(self.q) > 0


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()