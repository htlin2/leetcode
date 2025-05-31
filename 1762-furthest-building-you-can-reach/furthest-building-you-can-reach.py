class Solution:
    def furthestBuilding(self, nums: List[int], bricks: int, ladders: int) -> int:
        max_heap = [] # bricks
        for i in range(0, len(nums) - 1):
            curr_num = nums[i]
            next_num = nums[i + 1]
            delta = next_num - curr_num
            if delta <= 0: continue
            heapq.heappush(max_heap, -delta)
            bricks -= delta
            if bricks < 0:
                if not ladders: return i
                ladders -= 1
                bricks += -heapq.heappop(max_heap)
        return len(nums) - 1