class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        left = [] # max_heap
        right = [] # min_heap
        res = []
        for i in range(k):
            if not left or nums[i] <= -left[0]:
                heapq.heappush(left, -nums[i])
            else:
                heapq.heappush(right, nums[i])
            # balance
            if len(left) - len(right) >= 2:
                heapq.heappush(right, -heapq.heappop(left))
            elif len(right) - len(left) >= 1:
                heapq.heappush(left, -heapq.heappop(right))
        if k % 2 == 1:
            # odd
            median = -left[0]
        else:
            # even
            median = (-left[0] + right[0]) / 2
        res.append(median)
        balance_dict = collections.defaultdict(int)
        for i in range(k, len(nums)):
            prev_num = nums[i - k]
            balance_dict[prev_num] += 1
            # find balance
            balance = -1 if prev_num <= median else 1
            if not left or nums[i] <= median:
                balance += 1
                heapq.heappush(left, -nums[i])
            else:
                balance -= 1
                heapq.heappush(right, nums[i])
            if balance == 2:
                heapq.heappush(right, -heapq.heappop(left))
            elif balance == -2:
                heapq.heappush(left, -heapq.heappop(right))
            while left and balance_dict[-left[0]]:
                balance_dict[-left[0]] -= 1
                heapq.heappop(left)
            while right and balance_dict[right[0]]:
                balance_dict[right[0]] -= 1
                heapq.heappop(right)
            if k % 2 == 1:
                median = -left[0]
            else:
                median = (-left[0] + right[0]) / 2
            res.append(median)
        return res