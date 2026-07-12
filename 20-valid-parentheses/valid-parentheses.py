class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # 
        hashmap = {
            '(': ')',
            '[': ']',
            '{': '}',
        }
        for p in s:
            # handle open p
            if p in hashmap:
                stack.append(p)
                continue
            # handle close p
            if not stack:
                return False
            elif hashmap[stack[-1]] == p:
                stack.pop()
            else:
                return False
        return len(stack) == 0