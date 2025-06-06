class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t: return s
        t_counter = collections.Counter(t)
        left = 0
        window_counter = collections.defaultdict(int)
        balance = 0
        res = ''
        for right in range(len(s)):
            if s[right] in t_counter:
                window_counter[s[right]] += 1
                if window_counter[s[right]] == t_counter[s[right]]:
                    balance += 1
            while balance == len(t_counter):
                if not res or len(res) >= right - left + 1:
                    res = s[left:right + 1]
                if s[left] in window_counter:
                    if window_counter[s[left]] == t_counter[s[left]]:
                        balance -= 1
                    window_counter[s[left]] -= 1
                    if window_counter[s[left]] == 0:
                        del window_counter[s[left]]
                left += 1
        return res