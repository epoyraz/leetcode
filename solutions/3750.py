from bisect import bisect_left

class Solution(object):
    def solveQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        # Map each value to the sorted list of indices where it occurs
        positions = {}
        for i, v in enumerate(nums):
            positions.setdefault(v, []).append(i)
        
        # Ensure each list is sorted (though insertion order is increasing)
        # But to be safe if needed:
        # for v in positions:
        #     positions[v].sort()
        
        answer = []
        for q in queries:
            v = nums[q]
            pos_list = positions[v]
            if len(pos_list) == 1:
                # Only occurrence
                answer.append(-1)
                continue
            
            # Find the index of q in pos_list
            idx = bisect_left(pos_list, q)
            # Sanity: pos_list[idx] == q
            # Predecessor (circular)
            if idx > 0:
                pred = pos_list[idx - 1]
            else:
                pred = pos_list[-1]
            # Successor (circular)
            if idx + 1 < len(pos_list):
                succ = pos_list[idx + 1]
            else:
                succ = pos_list[0]
            
            # Compute minimal circular distance for both
            best = n  # large initial
            for j in (pred, succ):
                d = abs(j - q)
                circ = n - d
                best = min(best, d, circ)
            
            answer.append(best)
        
        return answer
