class Solution(object):
    def minimumCost(self, m, n, horizontalCut, verticalCut):
        """
        :type m: int
        :type n: int
        :type horizontalCut: List[int]
        :type verticalCut: List[int]
        :rtype: int
        """
        # Sort cuts in descending order so we always apply the largest next
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)
        
        # initially we have 1 horizontal segment and 1 vertical segment
        h_segs = 1
        v_segs = 1
        
        i = 0
        j = 0
        total = 0
        
        # Greedily pick the next largest cut
        while i < len(horizontalCut) and j < len(verticalCut):
            if horizontalCut[i] > verticalCut[j]:
                # cutting horizontally splits across all current vertical segments
                total += horizontalCut[i] * v_segs
                h_segs += 1
                i += 1
            else:
                # cutting vertically splits across all current horizontal segments
                total += verticalCut[j] * h_segs
                v_segs += 1
                j += 1
        
        # apply any remaining horizontal cuts
        while i < len(horizontalCut):
            total += horizontalCut[i] * v_segs
            i += 1
        
        # apply any remaining vertical cuts
        while j < len(verticalCut):
            total += verticalCut[j] * h_segs
            j += 1
        
        return total
