/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    // merge
    function merge(left, right) {
        let [i, j] = [0, 0]
        const res = []
        while (i < left.length && j < right.length) {
            if (left[i] <= right[j]) {
                res.push(left[i])
                i += 1
            } else {
                res.push(right[j])
                j += 1
            }
        }
        while (i < left.length) {            
            res.push(left[i])
            i += 1
        }
        while (j < right.length) {
            res.push(right[j])
            j += 1
        }
        return res
    }
    // split
    function split(nums) {
        if (nums.length <= 1) return nums
        const m = Math.floor((nums.length - 1) / 2)
        const left = split(nums.slice(0, m + 1))
        const right = split(nums.slice(m + 1))
        return merge(left, right)
    }
    const res = split(nums)
    for (let i = 0; i < nums.length; i++) {
        nums[i] = res[i]
    }
};