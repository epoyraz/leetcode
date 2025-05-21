class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        # Pre-fill the sets and collect empty cells
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r // 3) * 3 + (c // 3)].add(num)
                else:
                    empty.append((r, c))

        def backtrack(index):
            if index == len(empty):
                return True

            r, c = empty[index]
            box_idx = (r // 3) * 3 + (c // 3)

            for num in '123456789':
                if num not in rows[r] and num not in cols[c] and num not in boxes[box_idx]:
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_idx].add(num)

                    if backtrack(index + 1):
                        return True

                    # Undo the move
                    board[r][c] = '.'
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box_idx].remove(num)

            return False

        backtrack(0)
