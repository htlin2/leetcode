class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def helper(string):
            ans, temp = set(), ''
            for i, char in enumerate(string):
                temp += char
                if len(string) % (i + 1) != 0:
                    continue
                multiply = len(string) // len(temp)
                if temp * multiply == string:
                    ans.add(temp)
            return ans
        ans1 = helper(str1)
        ans2 = helper(str2)
        common = ans1.intersection(ans2)
        if not common: return ''
        res = ''
        for substr in common:
            if len(substr) > len(res):
                res = substr
        return res
"""
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

"""