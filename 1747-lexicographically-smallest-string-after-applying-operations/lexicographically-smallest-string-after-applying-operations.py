class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        def add(substr):
            res = list(substr)
            for i in range(len(res)):
                if i % 2:
                    res[i] = str((int(res[i]) + a) % 10)
            return ''.join(res)

        def rotate(substr):
            front = substr[:b]
            back = substr[b:]
            return back + front
        visited = set()
        def dfs(substr):
            if substr in visited: return
            visited.add(substr)
            added_substr = add(substr)
            dfs(added_substr)
            rotated_substr = rotate(substr)
            dfs(rotated_substr)
            return
        dfs(s)
        return sorted(list(visited))[0]
"""
backtracking
add a to odd idx
rotate s to right by b
"""