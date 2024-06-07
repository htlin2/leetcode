class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ''
        counter = collections.Counter(t)
        need, have = len(counter), 0
        window = collections.defaultdict(int)
        res = ''
        l = 0
        for r, char in enumerate(s):
            if char not in counter: continue
            window[char] += 1
            if window[char] == counter[char]:
                have += 1
            while need == have:
                if not res or len(res) > r - l + 1:
                    res = s[l:r + 1]
                if s[l] in counter:
                    window[s[l]] -= 1
                    if window[s[l]] < counter[s[l]]:
                        have -= 1
                l += 1
        return res