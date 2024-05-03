class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # case 2 tabulation
        prev_dp = collections.defaultdict(int)
        # iterate r through text2
        for r in range(len(text2)):
            # iterate c through text1
            dp = collections.defaultdict(int)
            for c in range(len(text1)):
                if text1[c] == text2[r]:
                    dp[c] = prev_dp[c - 1] + 1
                else:
                    dp[c] = max(prev_dp[c], dp[c - 1])
            prev_dp = dp
        return dp[len(text1) - 1]
        # time: O(n + m)
        # space:O(n)
        