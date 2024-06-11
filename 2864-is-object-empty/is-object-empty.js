/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    if (Array.isArray(obj)) {
        return obj.length === 0
    }
    const keys = Object.keys(obj)
    return keys.length === 0
};