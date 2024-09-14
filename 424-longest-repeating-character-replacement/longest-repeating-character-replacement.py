class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        N = len(s)
        window = collections.defaultdict(int) # char: count
        left, max_f, res = 0, 0, 0
        for right in range(N):
            char = s[right]
            window[char] += 1
            max_f = max(max_f, window[char])
            while (right - left + 1) - max_f > k:
                window[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res