class Solution:
    def reorganizeString(self, s: str) -> str:
        N = len(s)
        counter = collections.Counter(s)
        key_val_pairs = [[k, v] for k, v in counter.items()]
        sorted_freq = sorted(key_val_pairs, key=lambda t: t[-1], reverse=True)
        if sorted_freq[0][-1] > math.ceil(N / 2):
            return ''
        ans = [''] * N
        i = 0
        for k, v in sorted_freq:
            for _ in range(v):
                if i >= N:
                    i = 1
                ans[i] = k
                i += 2
        return ''.join(ans)