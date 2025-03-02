class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        instructions = instructions * 4
        directions = {
            0: (0, 1), # North
            180: (0, -1), # south
            90: (1, 0), # east
            270: (-1, 0), # west
        }
        facing = 0
        x, y = 0, 0
        hashmap = {}
        for i in range(2):
            path = [(x, y)] # (x, y)
            for d in instructions:
                if d == "G":
                    dx, dy = directions[facing]
                    x, y = path[-1]
                    x += dx
                    y += dy
                    path.append((x, y))
                elif d == 'L':
                    facing = (facing - 90 + 360) % 360
                elif d == 'R':
                    facing = (facing + 90 + 360) % 360
            hashmap[i] = path
        return True if hashmap[0] == hashmap[1] else False