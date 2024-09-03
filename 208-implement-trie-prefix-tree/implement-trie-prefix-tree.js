class TrieNode {
    constructor(val) {
        this.val = val
        this.children = {}
        this.isEnd = false
    }
}


var Trie = function() {
    this.root = new TrieNode('root')
};

/** 
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function(word) {
    let node = this.root
    for (char of word) {
        if (!(char in node.children)) {
            node.children[char] = new TrieNode(char)
        }
        node = node.children[char]
    }
    node.isEnd = true
};

/** 
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function(word) {
    let node = this.root
    for (char of word) {
        if (!(char in node.children)) return false
        node = node.children[char]
    }
    return node.isEnd
};

/** 
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function(prefix) {
    let node = this.root
    for (char of prefix) {
        if (!(char in node.children)) return false
        node = node.children[char]
    }
    return true
};

/** 
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */