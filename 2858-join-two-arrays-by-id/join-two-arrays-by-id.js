/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    const hashmap = arr1.reduce((acc, curr) => {
        acc[curr.id] = curr
        return acc
    }, {})
    arr2.forEach(e => {
        if (e.id in hashmap) {
            hashmap[e.id] = {
                ...hashmap[e.id],
                ...e
            }
        } else {
            hashmap[e.id] = e
        }
    })
    return Object.values(hashmap)
};