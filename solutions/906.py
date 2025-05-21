class Solution(object):
    def robotSim(self, commands, obstacles):
        direction = [(0,1), (1,0), (0,-1), (-1,0)]  # North, East, South, West
        dir_idx = 0
        x = y = 0
        max_dist = 0
        obstacle_set = set(map(tuple, obstacles))

        for cmd in commands:
            if cmd == -2:
                dir_idx = (dir_idx - 1) % 4
            elif cmd == -1:
                dir_idx = (dir_idx + 1) % 4
            else:
                dx, dy = direction[dir_idx]
                for _ in range(cmd):
                    if (x + dx, y + dy) in obstacle_set:
                        break
                    x += dx
                    y += dy
                    max_dist = max(max_dist, x*x + y*y)

        return max_dist
