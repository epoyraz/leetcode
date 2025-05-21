from collections import deque

class Solution:
    def catMouseGame(self, graph):
        N = len(graph)
        # 0 = unknown, 1 = mouse win, 2 = cat win
        dp = [[[0]*2 for _ in range(N)] for _ in range(N)]
        # degree[m][c][t]: number of moves available from state (m,c,t)
        degree = [[[0]*2 for _ in range(N)] for _ in range(N)]
        
        for m in range(N):
            for c in range(N):
                degree[m][c][0] = len(graph[m])                # mouseâs turn: all neighbors
                degree[m][c][1] = sum(1 for nc in graph[c]    # catâs turn: neighbors except hole 0
                                     if nc != 0)
        
        q = deque()
        # Initialize terminal states
        for i in range(N):
            for t in range(2):
                # mouse at hole â mouse wins
                dp[0][i][t] = 1
                q.append((0, i, t, 1))
                # cat catches mouse â cat wins
                dp[i][i][t] = 2
                q.append((i, i, t, 2))
        
        def parents(m, c, t):
            prev_t = 1 - t
            if t == 0:
                # arrived on mouse's turn â previous was cat move
                for pc in graph[c]:
                    if pc == 0: continue
                    yield (m, pc, prev_t)
            else:
                # arrived on cat's turn â previous was mouse move
                for pm in graph[m]:
                    yield (pm, c, prev_t)
        
        # Retrograde BFS
        while q:
            m, c, t, winner = q.popleft()
            for pm, pc, pt in parents(m, c, t):
                if dp[pm][pc][pt] != 0:
                    continue
                # If the player whose turn it is in the parent can move into a winning state for them:
                if (winner == 1 and pt == 0) or (winner == 2 and pt == 1):
                    dp[pm][pc][pt] = winner
                    q.append((pm, pc, pt, winner))
                else:
                    degree[pm][pc][pt] -= 1
                    # If all moves lead to opponent wins, then opponent wins here
                    if degree[pm][pc][pt] == 0:
                        lose = 2 if pt == 0 else 1
                        dp[pm][pc][pt] = lose
                        q.append((pm, pc, pt, lose))
        
        return dp[1][2][0]
