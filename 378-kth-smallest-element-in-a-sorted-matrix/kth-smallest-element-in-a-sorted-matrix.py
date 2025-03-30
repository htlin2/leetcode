class Solution:
    def kthSmallest(self, grid: List[List[int]], k: int) -> int:
        min_heap = [] # (num, (r, c))
        for i in range(len(grid[0])):
            heapq.heappush(min_heap, (grid[0][i], (0, i)))

        for _ in range(k - 1):
            _num, (r, c) = heapq.heappop(min_heap)
            if r + 1 < len(grid):
                num = grid[r + 1][c]
                to_add = (num, (r + 1, c))
                heapq.heappush(min_heap, to_add)
        return min_heap[0][0]
"""
heap + queue
k = 8
Input: grid = 
[
    [1,5,9],
    [10,11,13],
    [12,13,15]
]
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
k = 4
[ 1, 5, 9]
[10,11,13]
[12,]
"""