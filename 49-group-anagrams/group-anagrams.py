class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = collections.defaultdict(list)
        for word in strs:
            sorted_word = sorted(list(word))
            hashmap[''.join(sorted_word)].append(word)
        return hashmap.values()

"""
1) sort + hashmap
key: list()
abt: [bat]
ant: [nat, tan]
time: n * w log w
space: n

2) predefined index + hashmap
a: 1
b: 2
c: 3
[1, 0, 0, 1]
key = 1001
time: n
space: n
"""