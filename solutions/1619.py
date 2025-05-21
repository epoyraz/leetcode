class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        visited = set()
        x = y = 0
        visited.add((x, y))

        for direction in path:
            if direction == 'N':
                y += 1
            elif direction == 'S':
                y -= 1
            elif direction == 'E':
                x += 1
            elif direction == 'W':
                x -= 1

            if (x, y) in visited:
                return True
            visited.add((x, y))

        return False
