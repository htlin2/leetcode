class Solution:
    def compress(self, chars: List[str]) -> int:
        right = 0  # read pointer
        left = 0   # write pointer

        while right < len(chars):
            char = chars[right]
            count = 0

            # Count occurrences of the same character
            while right < len(chars) and chars[right] == char:
                right += 1
                count += 1

            # Write character
            chars[left] = char
            left += 1

            # Write count if greater than 1
            if count > 1:
                for c in str(count):
                    chars[left] = c
                    left += 1
        return left