class Solution:
    def is_valid(self, substr):
        stack = []
        for char in substr:
            if char == '(':
                stack.append(char)
            else:
                if not stack: return False
                stack.pop()
        return len(stack) == 0

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        q = collections.deque([''])
        while q:
            first = q.popleft()
            if len(first) == n * 2:
                if self.is_valid(first):
                    ans.append(first)
                continue
            q.append(first + '(')
            q.append(first + ')')
        return ans