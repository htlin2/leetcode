class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.row = 0
        self.col = -1

    def advance(self):
        self.col += 1
        while self.row < len(self.vec):
            if self.col >= len(self.vec[self.row]):
                self.col = 0
                self.row += 1
            elif self.vec[self.row][self.col] != None:
                return self.vec[self.row][self.col]
            else:
                self.col += 1


    def next(self) -> int:
        return self.advance()

    def hasNext(self) -> bool:
        col = self.col + 1
        row = self.row
        while row < len(self.vec):
            if col >= len(self.vec[row]):
                col = 0
                row += 1
            elif self.vec[row][col] != None:
                return True
            else:
                col += 1
        return False


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()