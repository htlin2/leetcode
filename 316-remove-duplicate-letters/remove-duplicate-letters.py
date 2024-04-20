class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # hashmap to keep {char: last_index}
        char_last_i = {}
        for i, char in enumerate(s):
            char_last_i[char] = i
        stack = [] # mono stack increasing
        # seen to keep track of chars in stack
        seen = set()
        # loop through s
        for i, char in enumerate(s):
            # continue current if char is already in stack
            if char in seen: continue
            # while stack and top stack is > s[i] and top stack can be seen later
            while stack and stack[-1] > char and char_last_i[stack[-1]] > i:
                top = stack.pop()
                seen.remove(top)
            seen.add(char)
            stack.append(char)
        return ''.join(stack)
"""
cbacdcbc
01234567
Output: "acdb"
{
    c: 7
    b: 6
    d: 4
    a: 2
}
monotonic increasing stack
stack = [a, c, d, b]
"""