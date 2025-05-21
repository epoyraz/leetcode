class Solution:
    def maximumWhiteTiles(self, tiles, carpetLen):
        # 1) Sort and unpack
        tiles.sort()
        l = [x for x,_ in tiles]
        r = [y for _,y in tiles]
        n = len(tiles)

        # 2) prefix_len[k] = total white tiles in intervals[0..k-1]
        prefix_len = [0] * (n+1)
        for i in range(n):
            prefix_len[i+1] = prefix_len[i] + (r[i] - l[i] + 1)

        ans = 0
        f = 0

        # 3) Sweep i and advance f
        for i in range(n):
            start = l[i]
            end_cover = start + carpetLen - 1

            # Ensure f >= i
            if f < i:
                f = i

            # Move f to first interval not fully covered
            while f < n and r[f] <= end_cover:
                f += 1

            # Fully covered total = prefix_len[f] - prefix_len[i]
            covered = prefix_len[f] - prefix_len[i]

            # Partial cover of interval f, if it overlaps
            if f < n and l[f] <= end_cover:
                covered += end_cover - l[f] + 1

            ans = max(ans, covered)

        return ans
