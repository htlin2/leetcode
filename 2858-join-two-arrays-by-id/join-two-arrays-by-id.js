/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    const hashmap = {} // key: {x: , y: }
    arr1.forEach(e => {
        hashmap[e.id] = e
    })
    arr2.forEach(e => {
        const id = e.id
        if (!id in hashmap) {
            hashmap[id] = e
            return
        }
        hashmap[id] = {
            ...hashmap[id],
            ...e
        }
    })
    return Object.values(hashmap)
};