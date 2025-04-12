class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = collections.Counter(t)
        window = collections.defaultdict(int)
        keys = 0
        left = 0
        res = ''
        for right in range(len(s)):
            if s[right] in counter:
                window[s[right]] += 1
                if window[s[right]] == counter[s[right]]:
                    keys += 1
            while keys == len(counter):
                if not res or len(res) >= right - left + 1:
                    substr = s[left:right+1]
                    res = substr
                if s[left] in counter:
                    if window[s[left]] == counter[s[left]]:
                        keys -= 1
                    window[s[left]] -= 1
                    if window[s[left]] == 0:
                        del window[s[left]]
                left += 1
        return res