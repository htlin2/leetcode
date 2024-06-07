/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    if (!n) return arr
    const res = []
    for (let i = 0; i < arr.length; i++) {
        if (!Array.isArray(arr[i])) {
            res.push(arr[i])
        } else {
            const flatten = flat(arr[i], n - 1)
            res.push(...flatten)
        }
    }
    return res
};