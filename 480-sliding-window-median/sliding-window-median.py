class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        left = [] # max_heap
        right = [] # min_heap
        res, heap_dict = [], collections.defaultdict(int)
        is_even = k % 2 == 0
        for i in range(k):
            if not left or nums[i] < -left[0]:
                heapq.heappush(left, -nums[i])
            else:
                heapq.heappush(right, nums[i])
            if len(left) - 1 > len(right):
                heapq.heappush(right, -heapq.heappop(left))
            if len(left) < len(right):
                heapq.heappush(left, -heapq.heappop(right))
        if is_even:
            median = (-left[0] + right[0]) / 2
        else:
            median = -left[0]
        res.append(median)
        for i in range(k, len(nums)):
            prev_num = nums[i - k]
            heap_dict[prev_num] += 1
            balance = -1 if prev_num <= median else 1
            if nums[i] <= median:
                balance += 1
                heapq.heappush(left, -nums[i])
            else:
                balance -= 1
                heapq.heappush(right, nums[i])
            # balance
            if balance < 0:
                heapq.heappush(left, -heapq.heappop(right))
            elif balance > 0:
                heapq.heappush(right, -heapq.heappop(left))
            # remove prev
            while left and heap_dict[-left[0]] > 0:
                heap_dict[-left[0]] -= 1
                heapq.heappop(left)
            while right and heap_dict[right[0]] > 0:
                heap_dict[right[0]] -= 1
                heapq.heappop(right)
            if is_even:
                median = (-left[0] + right[0]) / 2
            else:
                median = -left[0]
            res.append(median)
        return res

"""
left = -3, -1, 1
right = 3
"""