class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        stack = []
        for interval in intervals:
            if not stack:
                stack.append(interval)
                continue
            stack_l, stack_r = stack.pop()
            int_l, int_r = interval
            if stack_l <= int_l <= stack_r:
                stack_l = min(stack_l, int_l)
                stack_r = max(stack_r, int_r)
                stack.append([stack_l, stack_r])
                continue
            stack.append([stack_l, stack_r])
            stack.append([int_l, int_r])
        return stack
"""
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

[1, 3], [6, 9]
   2   5
[1,5], [6, 9 ]
stack = [1,5]
intervals = [6,9]
stack_l, stack_r = [1,3]
int_l, int_r = [2, 5]
res_l = min(stack_l, int_l)
res_r = max(stack_r, int_r)
T: O(n log n)
S: O(n)


Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]

[1,2],[3,5],[6,7],[8,10],[12,16]
        4          8
"""