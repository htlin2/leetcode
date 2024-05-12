class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        original_color = image[sr][sc]
        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS: return
            if image[r][c] != original_color or image[r][c] == color: return
            image[r][c] = color
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        dfs(sr, sc)
        return image
"""
dfs starting from image[r][c]
base case: return when image[r][c] != original_color
set image[r][c] = color
for loop to expand to 4 directions
    recursively call dfs with 4 directions
return image

Time: O(m * n)
Space: O(m * n)?? call stack
"""