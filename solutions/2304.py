class Solution:
    def cellsInRange(self, s):
        col1, row1, _, col2, row2 = s
        cols = [chr(i) for i in range(ord(col1), ord(col2) + 1)]
        rows = [str(i) for i in range(int(row1), int(row2) + 1)]
        
        result = []
        for col in cols:
            for row in rows:
                result.append(col + row)
        
        return result
