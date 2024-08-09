
var HitCounter = function() {
    this.cache = [] // (timestamp, counts)
};

/** 
 * @param {number} timestamp
 * @return {void}
 */
HitCounter.prototype.hit = function(timestamp) {
    const min_time = timestamp - 300
    while (this.cache.length && this.cache[0][0] <= min_time) {
        this.cache.shift()
    }
    if (this.cache.length && this.cache[this.cache.length - 1][0] === timestamp) {
        this.cache[this.cache.length - 1][1] += 1
    } else {
        this.cache.push([timestamp, 1])
    }
};

/** 
 * @param {number} timestamp
 * @return {number}
 */
HitCounter.prototype.getHits = function(timestamp) {
    const min_time = timestamp - 300
    while (this.cache.length && this.cache[0][0] <= min_time) {
        this.cache.shift()
    }
    let res = 0
    for (const tuple of this.cache) {
        const [key, value] = tuple
        res += value
    }
    return res
};

/** 
 * Your HitCounter object will be instantiated and called as such:
 * var obj = new HitCounter()
 * obj.hit(timestamp)
 * var param_2 = obj.getHits(timestamp)
 */