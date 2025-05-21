class Solution:
    def distinctNames(self, ideas):
        # Group suffixes by their first letter
        groups = [set() for _ in range(26)]
        for w in ideas:
            idx = ord(w[0]) - ord('a')
            groups[idx].add(w[1:])
        
        ans = 0
        # For each pair of different starting letters
        for i in range(26):
            si = groups[i]
            if not si:
                continue
            for j in range(i+1, 26):
                sj = groups[j]
                if not sj:
                    continue
                # Count common suffixes
                common = len(si & sj)
                # Valid swaps in ordered pairs: two directions
                count_i = len(si) - common
                count_j = len(sj) - common
                ans += 2 * count_i * count_j
        
        return ans
