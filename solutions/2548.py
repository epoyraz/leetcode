class Solution:
    def destroyTargets(self, nums, space):
        # Map residue -> (count, minimal num with that residue)
        stats = {}
        for x in nums:
            r = x % space
            if r not in stats:
                stats[r] = [0, x]
            stats[r][0] += 1
            if x < stats[r][1]:
                stats[r][1] = x
        
        # Find residue with max count (tie-break by minimal seed)
        best_count = -1
        answer = None
        for count, mn in stats.values():
            if count > best_count or (count == best_count and mn < answer):
                best_count = count
                answer = mn
        
        return answer
