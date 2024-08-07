
var MinStack = function() {
    this.stack = []
    this.minStack = []
};

/** 
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function(val) {
    if (!this.minStack.length) {
        this.minStack.push(val)
    } else {
        const mininum = Math.min(val, this.minStack[this.minStack.length - 1])
        this.minStack.push(mininum)
    }
    this.stack.push(val)
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    this.minStack.pop()
    this.stack.pop()
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    return this.stack[this.stack.length - 1]
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    return this.minStack[this.minStack.length - 1]
};

/** 
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */