/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    const stack = []
    let res = 0
    for (let i = 0; i < height.length; i++) {
        while (stack.length && height[stack[stack.length - 1]] < height[i]) {
            const top = stack.pop()
            if (!stack.length) break
            const h = Math.min(height[stack[stack.length - 1]], height[i]) - height[top]
            const base = i - [stack[stack.length - 1]] - 1
            res += base * h
        }
        stack.push(i)
    }
    return res
};

/*
monotonic stack decreasing
height = [0,1,0,2,1,0,1,3,2,1,2,1]
*/