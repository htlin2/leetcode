class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.ref = 0

class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def remove_word(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node.ref -= 1
                node = node.children[char]
        node.is_end = False

    def add_word(self, word):
        node = self.root
        for char in word:
            if not char in node.children:
                node.children[char] = TrieNode()
            node.ref += 1
            node = node.children[char]
        node.is_end = True

    def findWords(self, grid: List[List[str]], words: List[str]) -> List[str]:
        for word in words:
            self.add_word(word)
        ROW, COL = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set() # (r, c)
        res = set() # word

        def is_valid(r, c):
            if r < 0 or c < 0 or r >= ROW or c >= COL:
                return False
            if (r, c) in visited:
                return False
            return True

        def backtrack(r, c, node, substr):
            if node.is_end:
                res.add(substr)
                self.remove_word(substr)
            if not node.children or not is_valid(r, c) or not node.ref:
                return 
            char = grid[r][c]
            if char not in node.children:
                return 
            visited.add((r, c))
            for dr, dc in directions:
                nei_r, nei_c = r + dr, c + dc
                backtrack(nei_r, nei_c, node.children[char], substr + char)
            
            visited.remove((r, c))
            return

        for r in range(ROW):
            for c in range(COL):
                backtrack(r, c, self.root, '')
        return list(res)
"""
words = ["oath","pea","eat","rain"]
Input: board = [
    ["o","a","a","n"],
    ["e","t","a","e"],
    ["i","h","k","r"],
    ["i","f","l","v"]
], 
Output: ["eat","oath"]

Trie + Backtracking
construct Trie
          o     p      e
          a     e      a      
          t     a(end) t(end) \s
          h(end)               t(end)

visited = set() (r, c)
DFS(r, c, node, word):
    if node.is_end:
        add word to result
    check r c in grid
    run dfs on 4 directions

"""