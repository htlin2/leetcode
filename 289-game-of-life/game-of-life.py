class Solution:
    def gameOfLife(self, grid: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        {
            a: 0
            b: 1
            c: 0
            d: 1
        }
        {
            b,a
            0,0: a
            0,1: b
            1,0: c
            1,1: d
        }
        """
        hashmap = {'a': 0, 'b': 1, 'c': 0, 'd': 1}
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                counts = 0
                is_live = grid[r][c]
                for dr, dc in directions:
                    rr, cc = dr + r, dc + c
                    if rr < 0 or cc < 0 or rr >= ROWS or cc >= COLS:
                        continue
                    key = grid[rr][cc]
                    if key in hashmap and key in ['c', 'd']:
                        counts += 1
                    elif key not in hashmap:
                        counts += grid[rr][cc]
                if is_live and counts < 2:
                    grid[r][c] = 'c'
                elif is_live and counts in [2, 3]:
                    grid[r][c] = 'd'
                elif is_live and counts > 3:
                    grid[r][c] = 'c'
                elif not is_live and counts == 3:
                    grid[r][c] = 'b'
                else:
                    grid[r][c] = 'a'
        for r in range(ROWS):
            for c in range(COLS):
                grid[r][c] = hashmap[grid[r][c]]
        return