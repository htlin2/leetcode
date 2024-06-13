/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    const prefix = []
    let max_border = 0
    for (let i = 0; i < height.length; i++) {
        prefix.push(max_border)
        max_border = Math.max(height[i], max_border)
    }
    const postfix = []
    max_border = 0
    for (let i = height.length - 1; i >= 0; i--) {
        postfix.push(max_border)
        max_border = Math.max(height[i], max_border)
    }
    postfix.reverse()
    let res = 0
    for (let i = 0; i < height.length; i++) {
        const min_border = Math.min(prefix[i], postfix[i])
        res += Math.max(0, min_border - height[i])
    }
    return res
};

/*
prefix / postfix?
[0,1,0,2,1,0,1,3,2,1,2,1]
left > right
prefix = [0,0,1,1,2,2,2,2,3,3,3,3]
postfix= [3,3,3,3,3,3,3,2,2,2,1,0]
min    = [0,0,1,1,2,2,2,2,2,2,1,0]
min - h  [0,1,0,2,1,0,1,3,2,1,2,1]
water  = [0,0,1,0,1,2,1,0,0,1,0,0]

*/