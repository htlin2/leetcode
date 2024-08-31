/**
 * @param {string} s
 * @return {number}
 */
var calculate = function(s) {
    const stack = []
    let [sign, currSum, digits] = [1, 0, 0]
    for (const char of s) {
        if ('0123456789'.includes(char)) {
            digits = digits * 10 + Number(char)
        } else if ('+-'.includes(char)) {
            currSum += sign * digits
            digits = 0
            sign = char === '+' ? 1 : -1
        } else if (char === '(') {
            stack.push([currSum, sign])
            currSum = 0
            sign = 1
        } else if (char === ')') {
            currSum += sign * digits
            sign = 1
            digits = 0
            const [prevSum, prevSign] = stack.pop()
            currSum = prevSum + currSum * prevSign
        }
    }
    return currSum + sign * digits
};