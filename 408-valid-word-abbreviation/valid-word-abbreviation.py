class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if not abbr[j].isdigit():
                if word[i] != abbr[j]: return False
                i += 1
                j += 1
            elif abbr[j] == '0': return False
            else:
                k = j
                while k < len(abbr) and abbr[k].isdigit():
                    k += 1
                num = int(abbr[j:k])
                i += num
                j = k
        return i == len(word) and j == len(abbr)