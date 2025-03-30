class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        left = [] # max_heap
        right = [] # min_heap
        nums_dict = collections.defaultdict(int) # num: count
        is_odd = k % 2 == 1
        res = []
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
        for i in range(k, len(nums)):
            prev_num = nums[i - k]
            nums_dict[prev_num] += 1
            balance = -1 if prev_num <= median else 1
            if nums[i] <= median:
                heapq.heappush(left, -nums[i])
                balance += 1
            else:
                heapq.heappush(right, nums[i])
                balance -= 1
            if balance < 0:
                heapq.heappush(left, -heapq.heappop(right))
            elif 0 < balance:
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