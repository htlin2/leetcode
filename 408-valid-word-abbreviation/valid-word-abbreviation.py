class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if not abbr[j].isdigit():
                if word[i] == abbr[j]:
                    i += 1
                    j += 1
                    continue
                return False
            elif abbr[j] == '0':
                return False
            else:
                to_skip = 0
                while j < len(abbr) and abbr[j].isdigit():
                    to_skip = to_skip * 10 + int(abbr[j])
                    j += 1
                i += to_skip
        return i == len(word) and j == len(abbr)