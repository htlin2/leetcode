class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        visited = set()
        res = s
        def dfs(s):
            nonlocal res
            if s in visited: return
            visited.add(s)
            res = min(res, s)
            # add a
            s_arr = list(s)
            for i in range(1, len(s), 2):
                s_arr[i] = str((int(s_arr[i]) + int(a)) % 10)
            dfs(''.join(s_arr))
            # rotate b
            prefix = s[-b:]
            postfix = s[:-b]
            dfs(prefix + postfix)
            return
        dfs(s)
        return res