/**
 * @param {number} n
 * @return {number}
 */
var fib = function(n) {
    if (n < 2) return n
    return fib(n - 1) + fib(n - 2)
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