class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.curr = Node(homepage)
        self.head.next, self.curr.prev = self.curr, self.head
        self.tail.prev, self.curr.next = self.curr, self.tail

    def visit(self, url: str) -> None:
        self.curr.next = Node(url)
        prev = self.curr
        self.curr = self.curr.next
        self.curr.next, self.tail.prev = self.tail, self.curr
        self.curr.prev = prev

    def back(self, steps: int) -> str:
        while steps and self.curr.prev != self.head:
            steps -= 1
            self.curr = self.curr.prev
        return self.curr.val

    def forward(self, steps: int) -> str:
        while steps and self.curr.next != self.tail:
            steps -= 1
            self.curr = self.curr.next
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)