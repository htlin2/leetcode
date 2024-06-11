/**
 * @param {null|boolean|number|string|Array|Object} o1
 * @param {null|boolean|number|string|Array|Object} o2
 * @return {boolean}
 */
var areDeeplyEqual = function(o1, o2) {
    if (o1 === o2) return true
    if (o1 === null || o2 === null) return o1 === o2;
    if (typeof o1 !== typeof o2) return false;
    if (typeof o1 !== 'object' || typeof o2 !== 'object') return o1 === o2;
    // check array
    if (Array.isArray(o1) || Array.isArray(o2)) {
        if (!(Array.isArray(o1) && Array.isArray(o2))) return false
        if (o1.length !== o2.length) return false
        for (let i = 0; i < o1.length; i++) {
            if (!areDeeplyEqual(o1[i], o2[i])) return false
        }
        return true
    }
    // check object
    if (typeof o1 === 'object' && typeof o2 === 'object') {
        const o1Keys = Object.keys(o1)
        const o2Keys = Object.keys(o2)
        if (o1Keys.length !== o2Keys.length) return false
        for (let key of o1Keys) {
            if (!o2Keys.includes(key)) return false
            if (!areDeeplyEqual(o1[key], o2[key])) return false
        }
        return true
    }
    return false
};