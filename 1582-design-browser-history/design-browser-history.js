/**
 * @param {string} homepage
 */
var BrowserHistory = function(homepage) {
    this.bStacks = []
    this.curr = homepage
    this.fStacks = []
};

/** 
 * @param {string} url
 * @return {void}
 */
BrowserHistory.prototype.visit = function(url) {
    this.fStacks = []
    this.bStacks.push(this.curr.slice())
    this.curr = url
};

/** 
 * @param {number} steps
 * @return {string}
 */
BrowserHistory.prototype.back = function(steps) {
    while (this.bStacks.length && steps) {
        steps -= 1
        this.fStacks.push(this.curr.slice())
        this.curr = this.bStacks.pop()
    }
    return this.curr
};

/** 
 * @param {number} steps
 * @return {string}
 */
BrowserHistory.prototype.forward = function(steps) {
    while (this.fStacks.length && steps) {
        steps -= 1
        this.bStacks.push(this.curr.slice())
        this.curr = this.fStacks.pop()
    }
    return this.curr
};

/** 
 * Your BrowserHistory object will be instantiated and called as such:
 * var obj = new BrowserHistory(homepage)
 * obj.visit(url)
 * var param_2 = obj.back(steps)
 * var param_3 = obj.fStacks(steps)
 */