/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
    const hashmap = {
        1:    'I',
        4:    'IV',
        5:    'V',
        9:    'IX',
        10:    'X',
        40:    'XL',
        50:    'L',
        90:    'XC',
        100:    'C',
        400:    'CD',
        500:    'D',
        900:    'CM',
        1000:    'M'
    }
    const intRoman = Object.keys(hashmap).map(e => Number(e))
    intRoman.sort((a, b) => a < b).reverse()
    let res = ''
    for (const int of intRoman) {
        const counts = Math.floor(num / int)
        res += hashmap[int].repeat(counts)
        num %= int
    }
    return res
};