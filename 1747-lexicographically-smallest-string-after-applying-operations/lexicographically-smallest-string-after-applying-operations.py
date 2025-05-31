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
            sub_s = ''.join(s_arr)
            if sub_s not in visited:
                dfs(sub_s)
            # rotate b
            prefix = s[-b:]
            postfix = s[:-b]
            sub_s = prefix + postfix
            if sub_s not in visited:
                dfs(sub_s)
            return
        dfs(s)
        return res