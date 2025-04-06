class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        left = [] # max_heap -val
        right = [] # min_heap
        res = []
        is_odd = k % 2 == 1
        for i in range(k):
            if not left or nums[i] <= -left[0]:
                heapq.heappush(left, -nums[i])
            else:
                heapq.heappush(right, nums[i])
            if len(left) - len(right) >= 2:
                heapq.heappush(right, -heapq.heappop(left))
            if len(right) - len(left) >= 1:
                heapq.heappush(left, -heapq.heappop(right))
        if is_odd:
            median = -left[0]
        else:
            median = (-left[0] + right[0]) / 2
        res.append(median)
        nums_dict = collections.defaultdict(int)
        for i in range(k, len(nums)):
            prev_num = nums[i - k]
            nums_dict[prev_num] += 1
            balance = -1 if prev_num <= median else 1
            if nums[i] <= median:
                balance += 1
                heapq.heappush(left, -nums[i])
            else:
                balance -= 1
                heapq.heappush(right, nums[i])
            if balance < 0:
                heapq.heappush(left, -heapq.heappop(right))
            elif balance > 0:
                heapq.heappush(right, -heapq.heappop(left))
            while left and nums_dict[-left[0]]:
                nums_dict[-left[0]] -= 1
                heapq.heappop(left)
            while right and nums_dict[right[0]]:
                nums_dict[right[0]] -= 1
                heapq.heappop(right)
            if is_odd:
                median = -left[0]
            else:
                median = (-left[0] + right[0]) / 2
            res.append(median)
        return res
"""
left(min) = -1, 1, 3
right(max) = 3 
-3, -1, 1, 3
        m
"""