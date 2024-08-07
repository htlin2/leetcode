
var TimeMap = function() {
    this.cache = {} // key: [[time, value]]
};

/** 
 * @param {string} key 
 * @param {string} value 
 * @param {number} timestamp
 * @return {void}
 */
TimeMap.prototype.set = function(key, value, timestamp) {
    if (!this.cache[key]) {
        this.cache[key] = [[timestamp, value]]
    } else {
        this.cache[key].push([timestamp, value])
    }
};

/** 
 * @param {string} key 
 * @param {number} timestamp
 * @return {string}
 */
TimeMap.prototype.get = function(key, timestamp) {
    if (!this.cache[key]) return ''
    timeValues = this.cache[key]
    let l = 0
    let r = timeValues.length - 1
    while (l <= r) {
        let m = Math.floor((l + r) / 2)
        if (timeValues[m][0] === timestamp) return timeValues[m][1]
        if (timeValues[m][0] < timestamp) {
            l = m + 1
        } else {
            r = m - 1
        }
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