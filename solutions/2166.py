import itertools

class Solution:
    def countCombinations(self, pieces, positions):
        """
        :param pieces: List[str]           # e.g. ["rook","queen","bishop",...]
        :param positions: List[List[int]]  # 1-based coords [[r,c],...]
        :return: int                       # number of valid move combinations
        """
        # Movement directions for each piece type
        DIRS = {
            'rook':   [(1,0),(-1,0),(0,1),(0,-1)],
            'bishop': [(1,1),(1,-1),(-1,1),(-1,-1)],
            'queen':  [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)],
        }
        # 1) Precompute all possible destinations (including staying put)
        all_dests = []
        for ptype, (sr, sc) in zip(pieces, positions):
            dests = [(sr, sc)]
            for dr, dc in DIRS[ptype]:
                r, c = sr + dr, sc + dc
                while 1 <= r <= 8 and 1 <= c <= 8:
                    dests.append((r, c))
                    r += dr; c += dc
            all_dests.append(dests)

        def simulate(dest_combo):
            """Simulate simultaneous move; return False on any collision."""
            # Build movement info: (sr, sc, tr, tc, dr, dc, dist)
            steps = []
            for (sr, sc), (tr, tc) in zip(positions, dest_combo):
                dr = 0 if tr == sr else (1 if tr > sr else -1)
                dc = 0 if tc == sc else (1 if tc > sc else -1)
                dist = max(abs(tr - sr), abs(tc - sc))
                steps.append((sr, sc, tr, tc, dr, dc, dist))
            # Maximum time to simulate
            T = max(item[6] for item in steps)
            # Simulate each second
            for t in range(T + 1):
                seen = set()
                for sr, sc, tr, tc, dr, dc, dist in steps:
                    if t < dist:
                        r = sr + dr * t
                        c = sc + dc * t
                    else:
                        r, c = tr, tc
                    if (r, c) in seen:
                        return False
                    seen.add((r, c))
            return True

        # Count valid combinations
        ans = 0
        for dest_combo in itertools.product(*all_dests):
            if simulate(dest_combo):
                ans += 1
        return ans