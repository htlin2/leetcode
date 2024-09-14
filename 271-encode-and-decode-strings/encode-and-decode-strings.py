class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ''
        for word in strs:
            count = len(word)
            res += f"{count}#{word}"
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        start_idx = 0
        while start_idx < len(s):
            count = 0
            while s[start_idx].isdigit():
                count = count * 10 + int(s[start_idx])
                start_idx += 1

            start_idx += 1 # skip #
            end_idx = start_idx + count
            word = s[start_idx:end_idx]
            res.append(word)
            start_idx = end_idx
        return res
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))