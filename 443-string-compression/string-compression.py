class Solution:
    def compress(self, chars: List[str]) -> int:
        right = 0
        left = 0
        while right < len(chars):
            count = 1
            char = chars[right]
            while right + 1 < len(chars) and char == chars[right + 1]:
                right += 1
                count += 1
            right += 1
            chars[left] = char
            left += 1
            if count > 1:
                for c in str(count):
                    chars[left] = c
                    left += 1
        return left