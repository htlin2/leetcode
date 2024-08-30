/**
 * @param {number} n
 * @return {number}
 */
var fib = function(n) {
    const dp = Array(n + 1).fill(0)
    dp[1] = 1
    for (let i = 2; i <= n; i+=1) {
        dp[i] = dp[i - 1] + dp[i - 2]
    }
    return dp[n]
};

/*
1. dfs
base: if n < 2: return n
    dfs(n - 1) + dfs(n - 2)
2. dfs + memo
base: if n < 2: return n
    memo[i] = dfs(n - 1) + dfs(n - 2)
3. tabulation
    
4. optimized tabulation
*/