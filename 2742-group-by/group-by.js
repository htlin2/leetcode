/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    return this.reduce((acc, curr) => {
        const key = fn(curr)
        if (key in acc) {
            acc[key].push(curr)
        } else {
            acc[key] = [curr]
        }
        return acc
    }, {})
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */