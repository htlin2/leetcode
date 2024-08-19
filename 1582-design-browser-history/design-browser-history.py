class BrowserHistory:

    def __init__(self, homepage: str):
        self.prev = []
        self.next = []
        self.curr = homepage

    def visit(self, url: str) -> None:
        self.prev.append(self.curr[:])
        self.curr = url
        self.next = []

    def back(self, steps: int) -> str:
        while self.prev and steps:
            self.next.append(self.curr[:])
            self.curr = self.prev.pop()
            steps -= 1
        return self.curr

    def forward(self, steps: int) -> str:
        while self.next and steps:
            self.prev.append(self.curr[:])
            self.curr = self.next.pop()
            steps -= 1
        return self.curr


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)