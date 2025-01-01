class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        is_same = False
        for a in asteroids:
            while stack and stack[-1] >= 0 and a <= 0:
                last = stack.pop()
                if last == abs(a):
                    is_same = True
                    break
                if last > abs(a):
                    a = last
                else:
                    a = a
            if is_same:
                is_same = False
                continue
            stack.append(a)
        return stack

"""
stack
stack = [10,3]
Input: asteroids = [10,2,-5,3,-2]
Output: [10,3]

Time: O(n)
Space: O(n)

"""