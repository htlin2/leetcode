/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    if (!n) return arr
    const res = []
    for (const item of arr) {
        if (Array.isArray(item)) {
            // TODO: flat
            const flattened = flat(item, n - 1)
            res.push(...flattened)
        } else {
            res.push(item)
        }
    }
    return res
};