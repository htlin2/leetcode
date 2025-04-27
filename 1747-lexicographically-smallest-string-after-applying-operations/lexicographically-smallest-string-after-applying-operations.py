class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        combo = set()
        def dfs(s):
            if s in combo: return
            combo.add(s)
            # add or skip
            res = list(s)
            for i in range(len(s)):
                if i % 2 == 1:
                    int_num = (int(s[i]) + a) % 10
                    res[i] = str(int_num)
            dfs(''.join(res))
            # rotate or skip
            res = list(s)
            first = res[:b]
            second = res[-(len(s) - b):]
            res = second + first
            dfs(''.join(res))
            return
        dfs(s)
        sorted_combo = sorted(list(combo))
        return sorted_combo[0]