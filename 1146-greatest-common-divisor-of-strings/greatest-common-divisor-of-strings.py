class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def dfs(begin, end):
            if begin > end: return ''
            curr = str2[begin: end + 1]
            m1 = len(str2) // len(curr)
            m2 = len(str1) // len(curr)
            if (str2 == curr * m1) and (str1 == curr * m2):
                return curr
            return dfs(begin, end - 1)
        return dfs(0, len(str2) - 1)
            
"""
recurrsion
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
q = [ABCABC]
"""