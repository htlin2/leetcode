/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function(m, n) {
    const ROWS = m
    const COLS = n
    const directions = [[0, 1], [1, 0]]
    const memo = {}
    const dfs = (r, c) => {
        if (r === ROWS - 1 && c === COLS - 1) return 1
        const key = r + ',' + c;
        if (key in memo) return memo[key]
        let res = 0
        for (const [dr, dc] of directions) {
            const rr = dr + r
            const cc = dc + c
            if (rr >= ROWS || cc >= COLS) continue
            res += dfs(rr, cc)
        }
        memo[key] = res
        return res
    }
    return dfs(0, 0)
};