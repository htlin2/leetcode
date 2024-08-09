
var TimeMap = function() {
    this.cache = {} // key: [(timestamp, value), ()]
};

/** 
 * @param {string} key 
 * @param {string} value 
 * @param {number} timestamp
 * @return {void}
 */
TimeMap.prototype.set = function(key, value, timestamp) {
    if (key in this.cache) {
        this.cache[key].push([timestamp, value])
    } else {
        this.cache[key] = [[timestamp, value]]
    }
};

/** 
 * @param {string} key 
 * @param {number} timestamp
 * @return {string}
 */
TimeMap.prototype.get = function(key, timestamp) {
    // binary search weight left
    if (!this.cache[key]) return ''
    const timeValues = this.cache[key]
    const N = timeValues.length
    let l = 0
    let r = N - 1
    while (l <= r) {
        let m = Math.floor((l + r) / 2)
        if (timeValues[m][0] == timestamp) {
            r = m - 1
        } else if (timestamp < timeValues[m][0]) {
            r = m - 1
        } else {
            l = m + 1
        }
    }
    if (0 <= l && l < N && timeValues[l][0] === timestamp) {
        return timeValues[l][1]
    }
    if (l - 1 < 0) return ''
    return timeValues[l - 1][1]
};

/** 
 * Your TimeMap object will be instantiated and called as such:
 * var obj = new TimeMap()
 * obj.set(key,value,timestamp)
 * var param_2 = obj.get(key,timestamp)
 */