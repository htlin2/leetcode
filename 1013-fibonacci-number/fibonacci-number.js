/**
 * @param {number} n
 * @return {number}
 */
var fib = function(n) {
    if (n < 2) return n
    let prev = 0
    let curr = 1
    for (let i = 2; i <= n; i++) {
        const temp = prev + curr
        prev = curr
        curr = temp
    }
    return curr
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