class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        max_heap = []
        for i in range(len(heights) - 1):
            delta = heights[i + 1] - heights[i]
            if delta <= 0:
                continue
            elif bricks >= delta:
                bricks -= delta
                heapq.heappush(max_heap, -delta)
            elif ladders:
                ladders -= 1
                heapq.heappush(max_heap, -delta)
                bricks += -heapq.heappop(max_heap) - delta
            else:
                return i
        return len(heights) - 1