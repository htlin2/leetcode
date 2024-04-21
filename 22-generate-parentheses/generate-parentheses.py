class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # dfs backtracking
        ans, temp = [], []
        def dfs(open_p):
            if len(temp) == n * 2:
                if open_p == 0:
                    ans.append(''.join(temp))
                return
            if open_p < 0 or len(temp) > n * 2: return
            temp.append('(')
            dfs(open_p + 1)
            temp.pop()
            temp.append(')')
            dfs(open_p - 1)
            temp.pop()
        dfs(0)
        return ans
"""
n1    / \
     o1 o-1
   /\   
o2( o0) 
  /\     /\
o3( o1) o1 o-1
"""