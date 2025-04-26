class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        max_heap = []
        N = len(heights)
        for i in range(N - 1):
            if heights[i] >= heights[i + 1]:
                continue
            bricks_need = heights[i + 1] - heights[i]
            heapq.heappush(max_heap, -bricks_need)
            bricks -= bricks_need
            if bricks < 0:
                if not ladders:
                    return i
                ladders -= 1
                bricks += -heapq.heappop(max_heap)
        return N - 1
"""
max_heap = 5
Input: heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 1
Output: 7
[4,12,2,7,3,18,20,3,19]
      i 
"""