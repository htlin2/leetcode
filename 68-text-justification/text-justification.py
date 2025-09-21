class Solution:
    def fullJustify(self, words: List[str], max_width: int) -> List[str]:
        res = []
        width, line = 0, []
        i = 0
        while i < len(words):
            w = words[i]
            # next_w = '' if i + 1 >= len(words) else words[i + 1]
            # check if hit max width
            if width + len(line) + len(w) > max_width:
                total_spaces = max_width - width
                word_spaces = total_spaces // max(len(line) - 1, 1)
                rem_spaces = total_spaces % max(len(line) - 1, 1)
                for j in range(max(len(line) - 1, 1)):
                    line[j] += ' ' * word_spaces
                    if rem_spaces:
                        line[j] += ' '
                        rem_spaces -= 1
                res.append(''.join(line))
                width, line = 0, []
            # add w to current line
            width += len(w)
            line.append(w)
            i += 1
        # last line
        last_line = ' '.join(line)
        total_spaces = max_width - len(last_line)
        last_line += ' ' * total_spaces
        res.append(last_line)
        return res