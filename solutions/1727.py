class Solution:
    def canMouseWin(self, grid, catJump, mouseJump):
        from collections import deque, defaultdict

        rows, cols = len(grid), len(grid[0])
        MOUSE_TURN, CAT_TURN = 0, 1
        MOUSE_WIN, CAT_WIN, UNKNOWN = 1, 2, 0

        # 1) Collect all free cells and map to indices 0..P-1
        idx = {}
        cells = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != '#':
                    idx[(r, c)] = len(cells)
                    cells.append((r, c))

        P = len(cells)

        # 2) Find starts and food
        for (r, c), i in idx.items():
            if grid[r][c] == 'M':
                mouse_start = i
            elif grid[r][c] == 'C':
                cat_start = i
            elif grid[r][c] == 'F':
                food = i

        # 3) Precompute moves for mouse and cat from each cell
        DIRS = [(-1,0),(1,0),(0,-1),(0,1)]
        def build_moves(jump):
            nxt = [[] for _ in range(P)]
            prev = [[] for _ in range(P)]
            for i, (r0, c0) in enumerate(cells):
                # staying in place is allowed
                nxt[i].append(i)
                for dr, dc in DIRS:
                    for step in range(1, jump+1):
                        r, c = r0+dr*step, c0+dc*step
                        if 0 <= r < rows and 0 <= c < cols and grid[r][c] != '#':
                            j = idx[(r,c)]
                            nxt[i].append(j)
                        else:
                            break
                # we'll fill prev later
            for i in range(P):
                for j in nxt[i]:
                    prev[j].append(i)
            return nxt, prev

        mouse_nxt, mouse_prev = build_moves(mouseJump)
        cat_nxt,   cat_prev   = build_moves(catJump)

        # 4) degree[m][c][turn] = number of moves possible from that state
        degree = [[[0,0] for _ in range(P)] for __ in range(P)]
        for m in range(P):
            for c in range(P):
                degree[m][c][MOUSE_TURN] = len(mouse_nxt[m])
                degree[m][c][CAT_TURN]   = len(cat_nxt[c])

        # 5) result[m][c][turn] = UNKNOWN/MOUSE_WIN/CAT_WIN
        result = [[[UNKNOWN, UNKNOWN] for _ in range(P)] for __ in range(P)]
        q = deque()

        # 6) Initialize terminal states
        for m in range(P):
            for c in range(P):
                for t in (MOUSE_TURN, CAT_TURN):
                    if m == c:
                        result[m][c][t] = CAT_WIN
                        q.append((m, c, t, CAT_WIN))
                    elif c == food:
                        result[m][c][t] = CAT_WIN
                        q.append((m, c, t, CAT_WIN))
                    elif m == food:
                        result[m][c][t] = MOUSE_WIN
                        q.append((m, c, t, MOUSE_WIN))

        # 7) BFS retrograde propagation
        while q:
            m, c, turn, winner = q.popleft()
            # whose turn it was to move to get to (m,c,turn)?
            prev_turn = CAT_TURN if turn == MOUSE_TURN else MOUSE_TURN

            if prev_turn == MOUSE_TURN:
                # we came from a mouse move â cat_pos same, mouse_pos was one of mouse_prev[m]
                for pm in mouse_prev[m]:
                    if result[pm][c][prev_turn] != UNKNOWN:
                        continue
                    # If mouse just moved to a state that is MOUSE_WIN, mouse would choose it
                    if winner == MOUSE_WIN:
                        result[pm][c][prev_turn] = MOUSE_WIN
                        q.append((pm, c, prev_turn, MOUSE_WIN))
                    else:
                        # Every mouse move leads to CAT_WIN?
                        degree[pm][c][prev_turn] -= 1
                        if degree[pm][c][prev_turn] == 0:
                            result[pm][c][prev_turn] = CAT_WIN
                            q.append((pm, c, prev_turn, CAT_WIN))
            else:
                # prev_turn == CAT_TURN
                # we came from a cat move â mouse_pos same, cat_pos was one of cat_prev[c]
                for pc in cat_prev[c]:
                    if result[m][pc][prev_turn] != UNKNOWN:
                        continue
                    # If cat just moved to a state that is CAT_WIN, cat would choose it
                    if winner == CAT_WIN:
                        result[m][pc][prev_turn] = CAT_WIN
                        q.append((m, pc, prev_turn, CAT_WIN))
                    else:
                        # Every cat move leads to MOUSE_WIN?
                        degree[m][pc][prev_turn] -= 1
                        if degree[m][pc][prev_turn] == 0:
                            result[m][pc][prev_turn] = MOUSE_WIN
                            q.append((m, pc, prev_turn, MOUSE_WIN))

        # 8) Finally, starting from Mouseâs turn at the initial positions:
        return result[mouse_start][cat_start][MOUSE_TURN] == MOUSE_WIN
