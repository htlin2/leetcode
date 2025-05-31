class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {}
        for w in words:
            for char in w:
                adj[char] = set()
        for i in range(len(words) - 1):
            curr_word = words[i]
            next_word = words[i + 1]
            min_length = min(len(curr_word), len(next_word))
            for j in range(min_length):
                if curr_word[j] != next_word[j]:
                    adj[curr_word[j]].add(next_word[j])
                    break
            if len(curr_word) > len(next_word) and curr_word[:min_length] == next_word[:min_length]:
                return ''
        res = []
        visited = set()
        def dfs(char, cycle):
            if char in visited: return True
            if char in cycle: return False
            cycle.add(char)
            for nei in adj[char]:
                if not dfs(nei, cycle): return False
            visited.add(char)
            res.append(char)
            return True
        for char in adj.copy():
            if char in visited: continue
            if not dfs(char, set()):
                return ''
        return ''.join(res[::-1])