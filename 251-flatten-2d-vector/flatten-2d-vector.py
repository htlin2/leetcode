class Vector2D:

    def __init__(self, vec: List[List[int]]):
        def flat(arr):
            res = []
            if not arr: return []
            for num in arr:
                if isinstance(num, list):
                    res += flat(num)
                else:
                    res.append(num)
            return res
        self.q = collections.deque(flat(vec))

    def next(self) -> int:
        return self.q.popleft()

    def hasNext(self) -> bool:
        return len(self.q) != 0


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()