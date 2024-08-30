/**
 * @param {number} n
 * @return {number}
 */
var fib = function(n) {
    const memo = {}
    function fibMemo(n) {
        if (n in memo) return memo[n]
        if (n < 2) return n
        memo[n] = fibMemo(n - 1) + fibMemo(n - 2)
        return memo[n]
    }
    return fibMemo(n)
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