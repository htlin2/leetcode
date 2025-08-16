class Solution:
    def compress(self, chars: List[str]) -> int:
        left, right = 0, 0
        while right < len(chars):
            char = chars[right]
            count = 0
            while right < len(chars) and chars[right] == char:
                count += 1
                right += 1
            chars[left] = char
            left += 1
            if count > 1:
                for str_d in str(count):
                    chars[left] = str_d
                    left += 1
        return left

"""
two pointers?
"""