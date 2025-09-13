class Solution:
    def fullJustify(self, words: List[str], max_width: int) -> List[str]:
        res = []
        line, length = [], 0
        i = 0
        while i < len(words):
            if length + len(line) + len(words[i]) > max_width:
                # line complete
                spaces = (max_width - length) // max(1, len(line) - 1)
                rem = (max_width - length) % max(1, len(line) - 1)
                for j in range(max(1, len(line) - 1)):
                    line[j] += ' ' * spaces
                    if rem:
                        line[j] += ' '
                        rem -= 1
                res.append(''.join(line))
                line, length = [], 0
            line.append(words[i])
            length += len(words[i])
            i += 1
        # last line
        last_line = ' '.join(line)
        trailing_spaces = max_width - len(last_line)
        last_line += ' ' * trailing_spaces
        res.append(last_line)
        return res