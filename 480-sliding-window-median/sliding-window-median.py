class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        res = []
        left = [] # max_heap
        right = [] # min_heap
        for i in range(k):
            if not left or nums[i] <= -left[0]:
                heapq.heappush(left, -nums[i])
            else:
                heapq.heappush(right, nums[i])
            if len(left) - len(right) >= 2:
                heapq.heappush(right, -heapq.heappop(left))
            if len(right) - len(left) >= 1:
                heapq.heappush(left, -heapq.heappop(right))
        if k % 2 == 1:
            median = -left[0]
        else:
            median = (-left[0] + right[0]) / 2
        res.append(median)
        removed_nums = collections.defaultdict(int)
        for i in range(k, len(nums)):
            removed_num = nums[i - k]
            removed_nums[removed_num] += 1
            balance = -1 if removed_num <= median else 1
            if nums[i] <= median:
                balance += 1
                heapq.heappush(left, -nums[i])
            else:
                balance -= 1
                heapq.heappush(right, nums[i])
            if balance == -2:
                heapq.heappush(left, -heapq.heappop(right))
            if balance == 2:
                heapq.heappush(right, -heapq.heappop(left))
            while left and removed_nums[-left[0]]:
                removed_nums[-left[0]] -= 1
                heapq.heappop(left)
            while right and removed_nums[right[0]]:
                removed_nums[right[0]] -= 1
                heapq.heappop(right)
            if k % 2 == 1:
                median = -left[0]
            else:
                median = (-left[0] + right[0]) / 2
            res.append(median)
        return res