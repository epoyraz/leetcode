class Solution:
    def matrixSumQueries(self, n, queries):
        seen_rows = set()
        seen_cols = set()
        total = 0

        for t, idx, val in reversed(queries):
            if t == 0:  # row
                if idx not in seen_rows:
                    seen_rows.add(idx)
                    total += val * (n - len(seen_cols))
            else:  # column
                if idx not in seen_cols:
                    seen_cols.add(idx)
                    total += val * (n - len(seen_rows))
        return total
