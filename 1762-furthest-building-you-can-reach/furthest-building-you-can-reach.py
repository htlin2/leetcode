class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        max_heap = []
        for i in range(len(heights) - 1):
            delta = heights[i] - heights[i + 1]
            if delta >= 0:
                continue
            delta *= -1
            bricks -= delta
            heapq.heappush(max_heap, -delta)
            if bricks < 0:
                if ladders == 0:
                    return i
                ladders -= 1
                bricks += -heapq.heappop(max_heap)
        return len(heights) - 1