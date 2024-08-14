/**
 * @param {string} homepage
 */
var BrowserHistory = function(homepage) {
    this.prevStack = []
    this.nextStack = []
    this.curr = homepage
};

/** 
 * @param {string} url
 * @return {void}
 */
BrowserHistory.prototype.visit = function(url) {
    this.prevStack.push(this.curr.slice())
    this.curr = url
    this.nextStack = []
};

/** 
 * @param {number} steps
 * @return {string}
 */
BrowserHistory.prototype.back = function(steps) {
    while (this.prevStack.length && steps) {
        steps -= 1
        this.nextStack.push(this.curr.slice())
        this.curr = this.prevStack.pop()
    }
    return this.curr
};

/** 
 * @param {number} steps
 * @return {string}
 */
BrowserHistory.prototype.forward = function(steps) {
    while (this.nextStack.length && steps) {
        steps -= 1
        this.prevStack.push(this.curr.slice())
        this.curr = this.nextStack.pop()
    }
    return this.curr
};

/** 
 * Your BrowserHistory object will be instantiated and called as such:
 * var obj = new BrowserHistory(homepage)
 * obj.visit(url)
 * var param_2 = obj.back(steps)
 * var param_3 = obj.forward(steps)
 */