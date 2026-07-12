class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = collections.defaultdict(list) # key: []
        for w in strs:
            sorted_w = sorted(w)
            hashmap[''.join(sorted_w)].append(w)
        return [arr for arr in hashmap.values()]