class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        char_int_list = []
        digits = 0
        for char in abbr:
            if char.isdigit():
                digits *= 10
                digits += int(char)
                if digits == 0: return False
                continue
            if digits:
                char_int_list.append(digits)
                digits = 0
            char_int_list.append(char)
        if digits:
            char_int_list.append(digits)
        i, j = 0, 0
        while i < len(word) and j < len(char_int_list):
            if isinstance(char_int_list[j], int):
                i += char_int_list[j]
                j += 1
                continue
            if char_int_list[j] != word[i]:
                return False
            i += 1
            j += 1
        return i == len(word) and j == len(char_int_list)

"""
Input: word = "internationalization", abbr = "i12iz4n"

i 12 i z 4 n
j
i = 0
while i < N:
    if abbr[j] is digit:
        i += abbr[j]
        j += 1
        continue
    else:
        match word[i] == abbr[j]
        i += 1
        j += 1
"""