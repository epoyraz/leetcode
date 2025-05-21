from collections import Counter

class Solution(object):
    def canPartitionGrid(self, grid):
        m, n = len(grid), len(grid[0])

        total = 0
        right_cnt = Counter()
        for row in grid:
            total += sum(row)
            right_cnt.update(row)

        # --- horizontal cuts ---
        top_sum = 0
        top_cnt = Counter()
        bot_sum = total
        bot_cnt = right_cnt

        for k in range(m-1):
            row = grid[k]
            s = sum(row)
            top_sum += s
            bot_sum -= s
            top_cnt.update(row)
            for v in row:
                if bot_cnt[v] == 1:
                    del bot_cnt[v]
                else:
                    bot_cnt[v] -= 1

            if top_sum == bot_sum:
                return True

            A_sum, B_sum = (top_sum, bot_sum) if top_sum < bot_sum else (bot_sum, top_sum)
            delta = B_sum - A_sum
            heavier_is_bottom = (bot_sum > top_sum)

            # how many rows in the heavier piece?
            if heavier_is_bottom:
                start_row = k+1
                end_row = m-1
            else:
                start_row = 0
                end_row = k

            rows_cnt = end_row - start_row + 1

            # if it's at least 2Ã2, any cell works
            if rows_cnt > 1 and n > 1:
                cnt = bot_cnt if heavier_is_bottom else top_cnt
                if cnt.get(delta, 0):
                    return True
            else:
                # it's a vertical strip: endpoints at (start_row,0) and (end_row,0)
                if grid[start_row][0] == delta or grid[end_row][0] == delta:
                    return True

        # --- vertical cuts ---
        left_sum = 0
        left_cnt = Counter()
        right_sum = total
        right_cnt = Counter(v for row in grid for v in row)

        for c in range(n-1):
            col_vals = [grid[r][c] for r in range(m)]
            s = sum(col_vals)
            left_sum += s
            right_sum -= s
            left_cnt.update(col_vals)
            for v in col_vals:
                if right_cnt[v] == 1:
                    del right_cnt[v]
                else:
                    right_cnt[v] -= 1

            if left_sum == right_sum:
                return True

            A_sum, B_sum = (left_sum, right_sum) if left_sum < right_sum else (right_sum, left_sum)
            delta = B_sum - A_sum
            heavier_is_right = (right_sum > left_sum)

            if heavier_is_right:
                start_col = c+1
                end_col = n-1
            else:
                start_col = 0
                end_col = c

            cols_cnt = end_col - start_col + 1

            # at least 2Ã2
            if m > 1 and cols_cnt > 1:
                cnt = right_cnt if heavier_is_right else left_cnt
                if cnt.get(delta, 0):
                    return True
            else:
                # horizontal strip: endpoints at (0,start_col) and (m-1,start_col)
                if grid[0][start_col] == delta or grid[m-1][start_col] == delta:
                    return True

        return False
