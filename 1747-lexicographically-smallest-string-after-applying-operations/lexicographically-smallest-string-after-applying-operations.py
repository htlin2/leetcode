class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        combo = set()
        res = s
        def dfs(s):
            nonlocal res
            if s in combo: return
            combo.add(s)
            if s < res:
                res = s
            # add
            temp = list(s)
            for i in range(len(s)):
                if i % 2 == 1:
                    int_num = (int(s[i]) + a) % 10
                    temp[i] = str(int_num)
            dfs(''.join(temp))
            # rotate
            temp = s[-b:] + s[:-b]
            dfs(''.join(temp))
            return
        dfs(s)
        return res