class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = collections.Counter(magazine)
        for char in ransomNote:
            if char not in counter or counter[char] <= 0:
                return False
            counter[char] -= 1
        return True
"""
1) hashmap = {} key: letter from magazine, value: count
iterate through ransomNote
    if char not in hashmap or hashmap's value is less than 0
        return false
    decrement hashmap's value
Time: O(n)
space: O(1) -> 26 alphabets

2) brute force
iterate through ransomNote:
    if char is in magazine, remove charactor in magazine
Time: O(n * m)
space: O(1)
"""