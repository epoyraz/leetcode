class Solution:
    def unhappyFriends(self, n, preferences, pairs):
        # partner[i] = the friend paired with i
        partner = [0] * n
        for x, y in pairs:
            partner[x] = y
            partner[y] = x

        # rank[i][j] = how much i prefers j (lower is better)
        rank = [[0]*n for _ in range(n)]
        for i, prefs in enumerate(preferences):
            for idx, friend in enumerate(prefs):
                rank[i][friend] = idx

        unhappy = 0
        # check each friend x
        for x in range(n):
            y = partner[x]
            # go through all u that x prefers over y
            for u in preferences[x]:
                if u == y:
                    break
                v = partner[u]
                # if u prefers x over their partner v, x is unhappy
                if rank[u][x] < rank[u][v]:
                    unhappy += 1
                    break

        return unhappy
