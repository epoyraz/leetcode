class Solution:
    def distinctEchoSubstrings(self, text):
        n = len(text)
        # 64-bit mask
        mask = (1 << 64) - 1
        base = 1315423911

        # Precompute prefix hashes and powers
        h = [0] * (n + 1)
        p = [1] * (n + 1)
        for i, ch in enumerate(text):
            h[i+1] = ((h[i] * base) + (ord(ch))) & mask
            p[i+1] = (p[i] * base) & mask

        def get_hash(i, j):
            # hash of text[i:j]
            return (h[j] - (h[i] * p[j - i] & mask)) & mask

        seen = set()
        # iterate possible half-lengths
        for l in range(1, n // 2 + 1):
            # for each start of substring of length 2*l
            for i in range(0, n - 2*l + 1):
                if get_hash(i, i + l) == get_hash(i + l, i + 2*l):
                    seen.add(get_hash(i, i + 2*l))
        return len(seen)
