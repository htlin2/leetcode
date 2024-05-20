class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line, length = [], 0
        for w in words:
            # check line length
            if length + len(line) + len(w) > maxWidth:
                extra_spaces = maxWidth - length
                spaces = extra_spaces // max(1, len(line) - 1)
                remain = extra_spaces % max(1, len(line) - 1)
                # add space to line
                for i in range(max(1, len(line) - 1)):
                    line[i] += ' ' * spaces
                    if remain:
                        line[i] += ' '
                        remain -= 1
                # append line to res and reset line and length
                res.append(''.join(line))
                line, length = [], 0

            line.append(w)
            length += len(w)

        # logic about last_line
        last_line = ' '.join(line)
        # add trailing spaces
        last_line += ' ' * (maxWidth - len(last_line))
        res.append(last_line)
        return res