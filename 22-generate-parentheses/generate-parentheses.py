class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans, temp = [], []
        def dfs(op, cl):
            if cl < op or op < 0 or cl < 0: return
            if op == cl == 0:
                ans.append(''.join(temp))
                return
            temp.append('(')
            dfs(op - 1, cl)
            temp.pop()
            temp.append(')')
            dfs(op, cl - 1)
            temp.pop()
        dfs(n, n)
        return ans