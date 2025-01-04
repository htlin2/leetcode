class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        res = 0
        uniq_count = len(set(s))
        N = len(s)
        for target_uniq in range(1, uniq_count + 1):
            left = 0
            freq = collections.defaultdict(int)
            curr_uniq = 0
            count_at_least_k = 0

            for right in range(N):
                char = s[right]
                if freq[char] == 0:
                    curr_uniq += 1
                freq[char] += 1
                if freq[char] == k:
                    count_at_least_k += 1
                
                while curr_uniq > target_uniq:
                    if freq[s[left]] == k:
                        count_at_least_k -= 1
                    freq[s[left]] -= 1
                    if freq[s[left]] == 0:
                        curr_uniq -= 1
                    left += 1
                if curr_uniq == count_at_least_k:
                    res = max(res, right - left + 1)
        return res