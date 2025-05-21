class Solution:
    def executeInstructions(self, n, startPos, s):
        m = len(s)
        result = []

        dir_map = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

        for i in range(m):
            r, c = startPos
            steps = 0
            for j in range(i, m):
                dr, dc = dir_map[s[j]]
                r += dr
                c += dc
                if 0 <= r < n and 0 <= c < n:
                    steps += 1
                else:
                    break
            result.append(steps)

        return result
