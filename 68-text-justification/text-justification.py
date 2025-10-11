class Solution:
    def fullJustify(self, words: List[str], max_width: int) -> List[str]:
        res = []
        line, spaces = [], 0
        for w in words:
            # handle exceeding line
            if spaces + len(line) + len(w) > max_width:
                space_total = max_width - spaces
                space_count = space_total // max(len(line) - 1, 1)
                space_extra = space_total % max(len(line) - 1, 1)
                for i in range(max(len(line) - 1, 1)):
                    line[i] += ' ' * space_count
                    if space_extra:
                        space_extra -= 1
                        line[i] += ' '
                res.append(''.join(line))
                # rest line and spaces
                line, spaces = [], 0
            # add word to line
            line.append(w)
            spaces += len(w)
        # handle last line
        last_line = ' '.join(line)
        space_total = max_width - len(last_line)
        last_line += ' ' * space_total
        res.append(last_line)
        return res