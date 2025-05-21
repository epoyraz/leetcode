class Solution(object):
    def minValidStrings(self, words, target):
        """
        :type words: List[str]
        :type target: str
        :rtype: int
        """
        n = len(target)
        # 1) rollingâhash parameters
        mod1, mod2 = 10**9+7, 10**9+9
        base1, base2 = 91138233, 97266353

        # 2) determine max prefix length we care about
        max_w = 0
        for w in words:
            if len(w) > max_w:
                max_w = len(w)
        max_pref = min(max_w, n)
        if max_pref == 0:
            # If all words are empty or target empty (target nonempty by constraints),
            # we canât match any nonempty prefix â impossible
            return -1

        # 3) precompute powers up to max_pref
        p1 = [1] * (max_pref + 1)
        p2 = [1] * (max_pref + 1)
        for i in range(max_pref):
            p1[i+1] = (p1[i] * base1) % mod1
            p2[i+1] = (p2[i] * base2) % mod2

        # 4) build a list of sets: prefix_hash_sets[â] = { all hashes of wordâprefixes of length â }
        prefix_hash_sets = [set() for _ in range(max_pref + 1)]
        for w in words:
            h1 = h2 = 0
            limit = min(len(w), max_pref)
            for j in range(limit):
                c = ord(w[j])
                h1 = (h1 * base1 + c) % mod1
                h2 = (h2 * base2 + c) % mod2
                prefix_hash_sets[j+1].add((h1, h2))

        # 5) rollingâhash the target
        H1 = [0] * (n+1)
        H2 = [0] * (n+1)
        for i, ch in enumerate(target):
            c = ord(ch)
            H1[i+1] = (H1[i] * base1 + c) % mod1
            H2[i+1] = (H2[i] * base2 + c) % mod2

        def substring_hash(i, length):
            """Hash of target[i:i+length]."""
            x1 = (H1[i+length] - H1[i] * p1[length]) % mod1
            x2 = (H2[i+length] - H2[i] * p2[length]) % mod2
            return (x1, x2)

        # 6) for each i, binaryâsearch the longest valid prefix length â
        j_max = [i for i in range(n)]
        for i in range(n):
            rem = n - i
            hi = min(max_pref, rem)
            # quick reject
            if (substring_hash(i, 1) not in prefix_hash_sets[1]):
                continue

            lo = 1
            # find the largest â in [1..hi] with prefix_hash_sets[â] containing target[i:i+â]
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if substring_hash(i, mid) in prefix_hash_sets[mid]:
                    lo = mid
                else:
                    hi = mid - 1
            j_max[i] = i + lo

        # 7) JumpâGame II greedy to cover [0..n] with min jumps
        jumps = 0
        cur_end = 0
        farthest = 0
        for i in range(n):
            farthest = max(farthest, j_max[i])
            if i == cur_end:
                # need to take a new jump here
                if farthest <= i:
                    return -1
                jumps += 1
                cur_end = farthest
                if cur_end >= n:
                    break

        return jumps
