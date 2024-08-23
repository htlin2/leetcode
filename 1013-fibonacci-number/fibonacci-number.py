class Solution:
    def fib(self, n: int) -> int:
        prev, curr = 0, 1
        for _ in range(n):
            temp = curr + prev
            prev = curr
            curr = temp
        return prev
"""
1. recurrsion
    dfs
    base case: if n < 2: return n
    return n - 1 + n -2
    time: O(2 ^ n)
    space: O(n) 
2. recurrsion + memo
    save {n: result}
    add memo after base
    time: O(n)
    space: O(n)
3. dp - tabulation
    dp = []
    time: O(n)
    space: O(n)
4. while loop
    track prev, curr values
    time:O(n)
    space:O(1)
"""