class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                if abbr[j] == '0': return False
                idx = 0
                while j < len(abbr) and abbr[j].isdigit():
                    idx = 10 * idx + int(abbr[j])
                    j += 1
                i += idx
            else:
                if word[i] != abbr[j]: return False
                i, j = i + 1, j + 1
        return i == len(word) and j == len(abbr)
"""
two pointers
time: O(n) - longest length of n or m
space: O(1)
"""