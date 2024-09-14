class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        N = len(temp)
        res = [0] * N
        stack = [] # mono stack decreasing
        for i, t in enumerate(temp):
            while stack and temp[stack[-1]] < t:
                prev_idx = stack.pop()
                res[prev_idx] = i - prev_idx
            stack.append(i)
        return res
"""
Input: [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
 [1, 1  4  2  1  1        ] = output
  0  1  2  3  4  5  6  7
[73,74,75,71,69,72,76,73]
[        ,        ,76,73
monotonic stack decreasing
time: O(n)
space: O(n)
"""