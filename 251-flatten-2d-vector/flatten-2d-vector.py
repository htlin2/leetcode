class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.row = 0
        self.col = 0
        self.advance()

    def advance(self):
        while self.row < len(self.vec) and self.col >= len(self.vec[self.row]):
            self.row += 1
            self.col = 0

    def next(self) -> int:
        num = self.vec[self.row][self.col]
        self.col += 1
        self.advance()
        return num

    def hasNext(self) -> bool:
        return self.row < len(self.vec)


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()

"""
[
    [
        [
            [1, 2], [3], [4]]
        ], 
        [], [], [], [], [], [], []
    ]

"""