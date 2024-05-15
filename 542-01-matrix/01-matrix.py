class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        DIR = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        ROWS, COLS = len(mat), len(mat[0])
        q = collections.deque([])
        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    q.append([r, c])
                else:
                    mat[r][c] = '#'
        while q:
            r, c = q.popleft()
            for dr, dc in DIR:
                rr, cc = r + dr, c + dc
                if rr < 0 or cc < 0 or rr >= ROWS or cc >= COLS: continue
                if mat[rr][cc] != '#': continue
                mat[rr][cc] = mat[r][c] + 1
                q.append([rr, cc])
        return mat
"""
1. BFS

2. dp
"""