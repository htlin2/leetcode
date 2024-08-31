/**
 * @param {number} num
 * @return {string}
 */
const hashmap = {
    0: "Zero",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten",
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen",
    16: "Sixteen",
    17: "Seventeen",
    18: "Eighteen",
    19: "Nineteen",
    20: "Twenty",
    30: "Thirty",
    40: "Forty",
    50: "Fifty",
    60: "Sixty",
    70: "Seventy",
    80: "Eighty",
    90: "Ninety",
    100: "Hundred",
    1000: "Thousand",
    1000000: "Million",
    1000000000: "Billion"
}
var numberToWords = function(num) {
    if (num <= 20) return hashmap[num]
    if (num < 100) {
        const res = []
        const tenthCounts = Math.floor(num / 10) * 10
        res.push(hashmap[tenthCounts])
        if (num % 10) {
            const digits = numberToWords(num % 10);
            res.push(digits)
        }
        return res.join(' ')
    }
    if (num < 1000) {
        const res = []
        const houndredCounts = Math.floor(num / 100)
        res.push(numberToWords(houndredCounts), 'Hundred')
        if (num % 100) {
            res.push(numberToWords(num % 100))
        }
        return res.join(' ')
    }
    if (num < 1000000) {
        let res = []
        const thousandsCounts = Math.floor(num / 1000)
        res.push(numberToWords(thousandsCounts), 'Thousand')
        if (num % 1000) {
            res.push(numberToWords(num % 1000))
        }
        return res.join(' ')
    }
    if (num < 1000000000) {
        let res = []
        const leftCounts = Math.floor(num / 1000000)
        res.push(numberToWords(leftCounts), 'Million')
        if (num % 1000000) {
            res.push(numberToWords(num % 1000000))
        }
        return res.join(' ')
    }
    let res = []
    const leftCounts = Math.floor(num / 1000000000)
    res.push(numberToWords(leftCounts), 'Billion')
    if (num % 1000000000) {
        res.push(numberToWords(num % 1000000000))
    }
    return res.join(' ')
};