class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if not char in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        N = len(word)
        def dfs(node, j):
            for i in range(j, N):
                char = word[i]
                if char != '.':
                    if not char in node.children:
                        return False
                    node = node.children[char]
                else:
                    for nei in node.children.values():
                        if dfs(nei, i + 1):
                            return True
                    return False
            return node.is_end
        return dfs(self.root, 0)
    

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)