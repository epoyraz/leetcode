class Solution:
    def matchReplacement(self, s, sub, mappings):
        # Build mapping: old_char -> set of new_chars
        mp = {}
        for old, new in mappings:
            if old not in mp:
                mp[old] = set()
            mp[old].add(new)
        
        n, m = len(s), len(sub)
        # Try every possible starting position
        for i in range(n - m + 1):
            for j in range(m):
                sc = s[i + j]
                tc = sub[j]
                if sc == tc:
                    continue
                # else see if we can map tc -> sc
                if tc in mp and sc in mp[tc]:
                    continue
                # cannot match at this position
                break
            else:
                # completed all j without break
                return True
        return False
