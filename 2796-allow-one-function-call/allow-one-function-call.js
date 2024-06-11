/**
 * @param {Function} fn
 * @return {Function}
 */
class O {
    constructor(fn) {
        this.called = false
        this.fn = fn
    }

    Once(...args) {
        if (this.called) return
        this.called = true
        return this.fn(...args)
    }
}

var once = function(fn) {
    const Once = new O(fn)
    return function(...args) {
        return Once.Once(...args)
    }
};

/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */
