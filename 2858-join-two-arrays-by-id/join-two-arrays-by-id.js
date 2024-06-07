/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    const hashmap = {} // key: {x: , y: }
    arr1.forEach(e => {
        const id = e.id
        delete e.id
        hashmap[id] = e
    })
    arr2.forEach(e => {
        const id = e.id
        delete e.id
        if (!id in hashmap) {
            hashmap[id] = e
            return
        }
        hashmap[id] = {
            ...hashmap[id],
            ...e
        }
    })
    const res = []
    for (const [key, value] of Object.entries(hashmap)) {
        res.push({id: Number(key), ...value})
    }
    return res
};