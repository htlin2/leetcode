class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ''
        if len(s) < len(t): return ans
        counter = collections.Counter(t)
        need, have = len(counter), 0
        window = collections.defaultdict(int)
        l = 0
        for r, c in enumerate(s):
            if c not in counter: continue
            window[c] += 1
            if window[c] == counter[c]:
                have += 1
            while need == have:
                if not ans or len(ans) > r - l + 1:
                    ans = s[l:r+1]
                if s[l] in counter:
                    window[s[l]] -= 1
                    if window[s[l]] < counter[s[l]]:
                        have -=1
                l += 1
        return ans