
var HitCounter = function() {
    this.cache = []
};

/** 
 * @param {number} timestamp
 * @return {void}
 */
HitCounter.prototype.hit = function(timestamp) {
    this.cache.push(timestamp)
};

/** 
 * @param {number} timestamp
 * @return {number}
 */
HitCounter.prototype.getHits = function(timestamp) {
    // binary search weight right
    const N = this.cache.length
    const toFind = timestamp - 300
    let l = 0
    let r = N - 1
    while (l <= r) {
        let m = Math.floor((l + r) / 2)
        if (this.cache[m] <= toFind) {
            l = m + 1
        } else {
            r = m - 1
        }
    }
    return N - l
};

/** 
 * Your HitCounter object will be instantiated and called as such:
 * var obj = new HitCounter()
 * obj.hit(timestamp)
 * var param_2 = obj.getHits(timestamp)
 */