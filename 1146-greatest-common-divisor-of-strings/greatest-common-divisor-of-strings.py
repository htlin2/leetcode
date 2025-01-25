class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def reducer(substr):
            res = set()
            window = ''
            for right in range(len(substr)):
                window += substr[right]
                if len(substr) % len(window) == 0 and window * (len(substr) // len(window)) == substr:
                    res.add(window)
            return res
        reduced_1, reduced_2 = reducer(str1), reducer(str2)
        common_set = reduced_1.intersection(reduced_2)
        longest = ''
        for common in common_set:
            if len(common) >= len(longest):
                longest = common
        return longest

"""
sliding window

"""