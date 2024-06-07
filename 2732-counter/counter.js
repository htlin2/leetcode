/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    let value = n - 1
    return function() {
        value += 1
        return value
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */