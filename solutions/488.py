from collections import Counter, deque

class Solution:
    # fixed order of colours
    COLORS = ['R', 'Y', 'B', 'G', 'W']
    CID    = {c: i for i, c in enumerate(COLORS)}

    # --------------------------- RLE helpers ---------------------------
    @staticmethod
    def to_rle(s):
        """'RRBB' -> ((R,2),(B,2)) with colours as ints 0..4"""
        i, n, out = 0, len(s), []
        while i < n:
            j = i + 1
            while j < n and s[j] == s[i]:
                j += 1
            out.append((Solution.CID[s[i]], j - i))
            i = j
        return tuple(out)

    @staticmethod
    def shrink(rle):
        """drop runs â¥3, merge neighbours, repeat until stable"""
        changed = True
        while changed:
            changed, tmp = False, []
            # phase-1: drop long runs
            for c, k in rle:
                if k >= 3:
                    changed = True
                else:
                    tmp.append((c, k))
            # phase-2: merge neighbours (and drop newly â¥3)
            new = []
            for c, k in tmp:
                if new and new[-1][0] == c:
                    k += new.pop()[1]            # merged length
                if k >= 3:
                    changed = True
                else:
                    new.append((c, k))
            rle = tuple(new)
        return rle

    @staticmethod
    def solvable(rle, hand_t):
        """True if each colour on board can still reach 3 with remaining hand"""
        need = [0] * 5
        for c, k in rle:
            need[c] += k
        return all(need[c] == 0 or need[c] + hand_t[c] >= 3 for c in range(5))

    # ----------------------------- BFS --------------------------------
    def findMinStep(self, board, hand):
        start_rle  = self.shrink(self.to_rle(board))
        start_hand = tuple(Counter(hand)[c] for c in self.COLORS)

        dq   = deque([(start_rle, start_hand, 0)])     # (board, hand, steps)
        seen = { (start_rle, start_hand) }

        while dq:
            rle, hand_t, steps = dq.popleft()
            if not rle:                     # cleared the board
                return steps
            if not self.solvable(rle, hand_t):
                continue

            L = len(rle)

            # ---- A) boundary insertions (fill + boundary-bridge) ----
            for pos in range(L + 1):
                left  = rle[pos-1][0] if pos-1 >= 0 else None
                right = rle[pos][0]   if pos   <  L else None

                for col in range(5):
                    if hand_t[col] == 0:
                        continue
                    touch  = (left == col or right == col)
                    bridge = (left is not None and right is not None
                              and left == right and left != col)
                    if not touch and not bridge:
                        continue

                    runs = list(rle)
                    if left == col and right == col:           # fill middle
                        runs[pos-1] = (col, rle[pos-1][1] + 1 + rle[pos][1])
                        del runs[pos]
                    elif left == col:                          # extend left
                        runs[pos-1] = (col, rle[pos-1][1] + 1)
                    elif right == col:                         # extend right
                        runs[pos]   = (col, rle[pos][1]   + 1)
                    else:                                      # boundary bridge
                        runs.insert(pos, (col, 1))

                    shr   = self.shrink(tuple(runs))
                    new_h = list(hand_t); new_h[col] -= 1; new_h = tuple(new_h)
                    state = (shr, new_h)
                    if state not in seen:
                        seen.add(state)
                        dq.append((shr, new_h, steps + 1))

            # ---- B) split-bridge (inside a run â¥2 with different colour) ----
            for i, (c_run, k) in enumerate(rle):
                if k < 2:
                    continue
                for col in range(5):
                    if col == c_run or hand_t[col] == 0:
                        continue
                    runs = list(rle)
                    # split: run-colour (1), inserted ball, run-colour (k-1)
                    runs[i:i+1] = [(c_run, 1), (col, 1), (c_run, k - 1)]
                    shr   = self.shrink(tuple(runs))
                    new_h = list(hand_t); new_h[col] -= 1; new_h = tuple(new_h)
                    state = (shr, new_h)
                    if state not in seen:
                        seen.add(state)
                        dq.append((shr, new_h, steps + 1))

        return -1                          # impossible to clear
