class Solution:
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        cells = [[i, j] for i in range(rows) for j in range(cols)]
        cells.sort(key=lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter))
        return cells
