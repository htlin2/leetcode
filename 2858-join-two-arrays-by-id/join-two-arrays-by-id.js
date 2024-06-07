/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    const hashmap = {} // key: {x: , y: }
    arr1.forEach(e => hashmap[e.id] = e)
    arr2.forEach(e => {
        if (e.id in hashmap) {
            hashmap[e.id] = {
                ...hashmap[e.id],
                ...e
            }
            return
        }
        hashmap[e.id] = e
    })
    return Object.values(hashmap)
};