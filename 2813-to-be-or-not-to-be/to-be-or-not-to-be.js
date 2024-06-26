/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    function toBe(val2) {
        if (val === val2) return true
        throw Error("Not Equal")
    }
    function notToBe(val3) {
        if (val !== val3) return true
        throw Error("Equal")
    }
    return {toBe, notToBe}
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */