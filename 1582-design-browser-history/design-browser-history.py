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
        self.head.next, self.tail.prev = self.curr, self.curr
        self.curr.next, self.curr.prev = self.tail, self.head

    def visit(self, url: str) -> None:
        node = Node(url)
        self.curr.next, self.tail.prev = node, node
        node.prev, node.next = self.curr, self.tail
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        while self.curr.prev != self.head and steps:
            self.curr = self.curr.prev
            steps -= 1        
        return self.curr.val

    def forward(self, steps: int) -> str:
        while self.curr.next != self.tail and steps:
            self.curr = self.curr.next
            steps -= 1        
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)