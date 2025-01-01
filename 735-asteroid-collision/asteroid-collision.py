class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0:
                if stack[-1] == abs(a):
                    stack.pop()
                    break
                elif stack[-1] > abs(a):
                    break
                else:
                    stack.pop()
            else:
                stack.append(a)
        return stack