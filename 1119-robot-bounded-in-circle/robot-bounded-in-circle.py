class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        hashmap = {
            0: (0, 1), # north
            90: (1, 0), # east
            180: (0, -1), # south
            270: (-1, 0), # west
        }
        paths = {}
        instructions *= 4
        facing = 0
        x, y = 0, 0
        for i in range(2):
            path = [(x, y)]
            for instruction in instructions:
                if instruction == 'G':
                    dx, dy = hashmap[facing]
                    x += dx
                    y += dy
                    path.append((x, y))
                elif instruction == 'R':
                    facing = (facing + 90) % 360
                elif instruction == 'L':
                    facing = (facing - 90 + 360) % 360
            paths[i] = path
        return paths[0] == paths[1]