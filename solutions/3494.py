class Solution(object):
    def minimumCost(self, m, n, horizontalCut, verticalCut):
        """
        :type m: int
        :type n: int
        :type horizontalCut: List[int]
        :type verticalCut: List[int]
        :rtype: int
        """
        # sort descending
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)
        
        h_idx = 0
        v_idx = 0
        h_segments = 1
        v_segments = 1
        total = 0
        
        # Greedily do the largest remaining cut
        while h_idx < len(horizontalCut) and v_idx < len(verticalCut):
            if horizontalCut[h_idx] > verticalCut[v_idx]:
                total += horizontalCut[h_idx] * v_segments
                h_segments += 1
                h_idx += 1
            else:
                total += verticalCut[v_idx] * h_segments
                v_segments += 1
                v_idx += 1
        
        # Remaining horizontal cuts
        while h_idx < len(horizontalCut):
            total += horizontalCut[h_idx] * v_segments
            h_segments += 1
            h_idx += 1
        
        # Remaining vertical cuts
        while v_idx < len(verticalCut):
            total += verticalCut[v_idx] * h_segments
            v_segments += 1
            v_idx += 1
        
        return total
