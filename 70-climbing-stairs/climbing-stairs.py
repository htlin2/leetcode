class Solution:
    def climbStairs(self, n: int) -> int:
        prev, curr = 0, 1
        for i in range(n):
            temp = curr
            curr = curr + prev
            prev = temp
        return curr

"""
n = 2
0 1 2
1 1 2   

n = 3
0 1 2 3
1 1 2 3

"""