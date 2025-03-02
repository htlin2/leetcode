class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # North, East, South, West
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y, d = 0, 0, 0
        for i in instructions:
            if i == 'G':
                x += directions[d][0]
                y += directions[d][1]
            elif i == 'R':
                d = (d + 1) % 4
            elif i == 'L':
                d = (d - 1) % 4
        return (x == 0 and y == 0) or d != 0