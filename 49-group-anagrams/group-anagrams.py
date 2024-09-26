import collections
class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        hashmap = collections.defaultdict(list) # sorted_key: list of word
        for w in words:
            key = ''.join(sorted(w))
            hashmap[key].append(w)
        return hashmap.values()

"""
hashmap + sort
Time: O(n * w log w)
Space: O(n)
"""