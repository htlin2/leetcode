class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(left, right):
            while left <= right:
                if s[left] != s[right]: return False
                left += 1
                right -= 1
            return True
        res = []
        def backtrack(i, str_list):
            if i >= len(s):
                res.append(str_list[::])
                return
            for j in range(i, len(s)):
                if is_palindrome(i, j):
                    str_list.append(s[i:j + 1])
                    backtrack(j + 1, str_list)
                    str_list.pop()
        backtrack(0, [])
        return res


"""
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
  
  a aa aab(x) 
  a  b
  b
  
input = aaab
 a    aa      aaa
 a ab(x) a     b
 a       b
 b
"""