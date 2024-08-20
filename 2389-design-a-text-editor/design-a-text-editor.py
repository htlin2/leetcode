class TextEditor:

    def __init__(self):
        self.left = []
        self.right = []

    def _get_last_ten(self):
        return ''.join(self.left[-10:])

    def addText(self, text: str) -> None:
        for t in text:
            self.left.append(t)        

    def deleteText(self, k: int) -> int:
        counts = min(k, len(self.left))
        res = counts
        while counts:
            counts -= 1
            self.left.pop()
        return res

    def cursorLeft(self, k: int) -> str:
        counts = min(k, len(self.left))
        while counts:
            counts -= 1
            self.right.append(self.left.pop())
        return self._get_last_ten()

    def cursorRight(self, k: int) -> str:
        counts = min(k, len(self.right))
        while counts:
            counts -= 1
            self.left.append(self.right.pop())
        return self._get_last_ten()


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)