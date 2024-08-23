class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if not abbr[j].isdigit():
                if word[i] != abbr[j]: 
                    return False
                i += 1
                j += 1
            elif abbr[j] == '0': 
                return False
            else:
                digits = 0
                while j < len(abbr) and abbr[j].isdigit():
                    digits = digits * 10 + int(abbr[j])
                    j += 1
                i += digits
        return i == len(word) and j == len(abbr)