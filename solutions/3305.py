class Solution(object):
    def countPrefixSuffixPairs(self, words):
        # two independent rollingâhashes to avoid 64-bit collisions
        B1, B2 = 91138233, 97266353
        MOD1, MOD2 = 10**9+7, 10**9+9

        # seen_by_len[len] = { (h1, h2): count_of_words_of_that_hash_and_len }
        seen_by_len = {}
        result = 0

        for w in words:
            n = len(w)

            # 1) build prefix hashes h1, h2
            h1 = [0] * (n + 1)
            h2 = [0] * (n + 1)
            v1 = v2 = 0
            for i, ch in enumerate(w, 1):
                code = ord(ch)
                v1 = (v1 * B1 + code) % MOD1
                v2 = (v2 * B2 + code) % MOD2
                h1[i] = v1
                h2[i] = v2

            # 2) build KMP pi array
            pi = [0] * n
            for i in range(1, n):
                j = pi[i-1]
                while j and w[i] != w[j]:
                    j = pi[j-1]
                if w[i] == w[j]:
                    j += 1
                pi[i] = j

            # 3) walk *all* borders â = n, Ï[n-1], Ï[Ï[n-1]-1], â¦ > 0
            border = n
            while border > 0:
                d = seen_by_len.get(border)
                if d:
                    result += d.get((h1[border], h2[border]), 0)
                border = pi[border-1]

            # 4) record this full word under its length
            key = (h1[n], h2[n])
            bucket = seen_by_len.setdefault(n, {})
            bucket[key] = bucket.get(key, 0) + 1

        return result
