class Solution:
    def rotateTheBox(self, box):
        m, n = len(box), len(box[0])
        # apply gravity to each row (stones fall to the right until obstacles)
        new_box = []
        for i in range(m):
            new_row = ['.'] * n
            write = n - 1
            for j in range(n - 1, -1, -1):
                if box[i][j] == '*':
                    new_row[j] = '*'
                    write = j - 1
                elif box[i][j] == '#':
                    new_row[write] = '#'
                    write -= 1
            new_box.append(new_row)
        # rotate 90 degrees clockwise
        res = [[None] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                res[j][m - 1 - i] = new_box[i][j]
        return res
