/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
    if (!intervals.length) return []
    intervals.sort((a, b) => a[0] - b[0])
    const stack = []
    for (let i = 0; i < intervals.length; i++) {
        if (i === 0) {
            stack.push(intervals[i])
            continue
        }
        const [sBegin, sEnd] = stack[stack.length - 1]
        const [iBegin, iEnd] = intervals[i]
        const isOverlap = (sBegin <= iBegin && iBegin <= sEnd) || (iBegin <= sBegin && sBegin <= iEnd)
        if (isOverlap) {
            stack.pop()
            stack.push([Math.min(sBegin, iBegin), Math.max(sEnd, iEnd)])
        } else {
            stack.push(intervals[i])
        }
    }
    return stack
};

`
input = [[1,3],[2,6],[8,10],[15,18]]
output =[[1,6],[8,10],[15,18]]
[1,      6   
            8    10
                    15   18
stack = [[1, 6], [8, 10], ]
`