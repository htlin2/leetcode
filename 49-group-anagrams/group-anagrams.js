/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(words) {
    const hashmap = {}
    for(const word of words) {
        const sortedWord = word.split('').sort().join('')
        if (!(hashmap[sortedWord])) {
            hashmap[sortedWord] = []
        }
        hashmap[sortedWord].push(word)
    }
    return Object.values(hashmap)
};

// `
// Input: strs = ["eat","tea","tan","ate","nat","bat"]
// Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


// hashmap = {} key: sorted word, value: [word1, word2]
// loop through strs:
//     eat -> aet
//     hashmap[aet]: [eat]

//     tea -> aet
//     hashmap[aet]: [eat, tea]

//     bat -> abt
//     hashmap[aet]: [eat, tea]
//     hashmap[abt]: [bat]

// time: O(n + w log w)
// space: O(n + w)
// `