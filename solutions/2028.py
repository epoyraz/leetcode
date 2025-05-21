class Solution:
    def earliestAndLatest(self, n, firstPlayer, secondPlayer):
        first, second = firstPlayer, secondPlayer
        memo = {}

        def solve(players):                       # players: tuple, ascending IDs
            key = players
            if key in memo:
                return memo[key]

            # positions (1-indexed) of the two stars
            try:
                pa = players.index(first) + 1
                pb = players.index(second) + 1
            except ValueError:
                # one of them is already eliminated â invalid branch
                return (float('inf'), 0)

            if pa + pb == len(players) + 1:       # they meet this round
                return (1, 1)

            best = [float('inf'), 0]              # [earliest, latest]

            half = len(players) // 2
            mid_exists = len(players) % 2 == 1
            mid_player = players[half] if mid_exists else None

            winners_seen = set()                  # avoid duplicate next states

            def backtrack(idx, curr):
                if idx >= half:
                    # append middle auto-advance if odd
                    if mid_exists:
                        curr.append(mid_player)
                    nxt = tuple(sorted(curr))     # winners lined up ascending
                    if nxt not in winners_seen:
                        winners_seen.add(nxt)
                        e, l = solve(nxt)
                        if e != float('inf'):
                            best[0] = min(best[0], e + 1)
                            best[1] = max(best[1], l + 1)
                    if mid_exists:
                        curr.pop()
                    return

                left = players[idx]
                right = players[-1 - idx]

                # if this pair contains exactly the two stars, they meet now (handled earlier)
                if (left == first and right == second) or (left == second and right == first):
                    return

                # if pair involves one star, that star must win
                if left == first or left == second:
                    curr.append(left)
                    backtrack(idx + 1, curr)
                    curr.pop()
                elif right == first or right == second:
                    curr.append(right)
                    backtrack(idx + 1, curr)
                    curr.pop()
                else:
                    # branch: left wins or right wins
                    curr.append(left)
                    backtrack(idx + 1, curr)
                    curr.pop()
                    curr.append(right)
                    backtrack(idx + 1, curr)
                    curr.pop()

            backtrack(0, [])
            memo[key] = tuple(best)
            return memo[key]

        initial_players = tuple(range(1, n + 1))
        return list(solve(initial_players))
