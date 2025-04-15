class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        is_odd = k % 2 == 1
        left = [] # max_heap
        right = [] # min_heap
        res = []
        for i in range(k):
            if not left or nums[i] <= -left[0]:
                heapq.heappush(left, -nums[i])
            else:
                heapq.heappush(right, nums[i])
            if len(left) - len(right) > 1:
                heapq.heappush(right, -heapq.heappop(left))
            elif len(right) - len(left) > 0:
                heapq.heappush(left, -heapq.heappop(right))
        if is_odd:
            median = -left[0]
        else:
            median = (-left[0] + right[0]) / 2
        balance_dict = collections.defaultdict(int)
        res.append(median)
        for i in range(k, len(nums)):
            prev_num = nums[i - k]
            balance_dict[prev_num] += 1
            balance = -1 if prev_num <= median else 1
            if nums[i] <= median:
                balance += 1
                heapq.heappush(left, -nums[i])
            elif nums[i] > median:
                balance -= 1
                heapq.heappush(right, nums[i])
            if balance < 0:
                heapq.heappush(left, -heapq.heappop(right))
            if balance > 0:
                heapq.heappush(right, -heapq.heappop(left))
            while left and balance_dict[-left[0]]:
                balance_dict[-left[0]] -= 1
                heapq.heappop(left)
            while right and balance_dict[right[0]]:
                balance_dict[right[0]] -= 1
                heapq.heappop(right)
            if is_odd:
                median = -left[0]
            else:
                median = (-left[0] + right[0]) / 2
            res.append(median)
        return res