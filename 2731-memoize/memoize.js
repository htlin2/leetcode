/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    let memo = {}
    return function(...args) {
        const key = JSON.stringify(args)
        if (key in memo) return memo[key]
        const res = fn(...args)
        memo[key] = res
        return res
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */