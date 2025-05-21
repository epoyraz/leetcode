class Solution(object):
    def minimumDistance(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        # Precompute transformed coords
        u = [x + y for x, y in points]
        v = [x - y for x, y in points]
        
        # Find max_u, second_max_u, count_max_u
        max_u = -10**30
        second_max_u = -10**30
        count_max_u = 0
        
        # Find min_u, second_min_u, count_min_u
        min_u = 10**30
        second_min_u = 10**30
        count_min_u = 0
        
        for val in u:
            # max
            if val > max_u:
                second_max_u = max_u
                max_u = val
                count_max_u = 1
            elif val == max_u:
                count_max_u += 1
            elif val > second_max_u:
                second_max_u = val
            
            # min
            if val < min_u:
                second_min_u = min_u
                min_u = val
                count_min_u = 1
            elif val == min_u:
                count_min_u += 1
            elif val < second_min_u:
                second_min_u = val
        
        # Same for v
        max_v = -10**30
        second_max_v = -10**30
        count_max_v = 0
        
        min_v = 10**30
        second_min_v = 10**30
        count_min_v = 0
        
        for val in v:
            if val > max_v:
                second_max_v = max_v
                max_v = val
                count_max_v = 1
            elif val == max_v:
                count_max_v += 1
            elif val > second_max_v:
                second_max_v = val
            
            if val < min_v:
                second_min_v = min_v
                min_v = val
                count_min_v = 1
            elif val == min_v:
                count_min_v += 1
            elif val < second_min_v:
                second_min_v = val
        
        # Now try removing each point
        ans = float('inf')
        for i in range(n):
            # Compute new u-range
            ui = u[i]
            if ui == max_u and count_max_u == 1:
                new_max_u = second_max_u
            else:
                new_max_u = max_u
            
            if ui == min_u and count_min_u == 1:
                new_min_u = second_min_u
            else:
                new_min_u = min_u
            
            A_i = new_max_u - new_min_u
            
            # Compute new v-range
            vi = v[i]
            if vi == max_v and count_max_v == 1:
                new_max_v = second_max_v
            else:
                new_max_v = max_v
            
            if vi == min_v and count_min_v == 1:
                new_min_v = second_min_v
            else:
                new_min_v = min_v
            
            B_i = new_max_v - new_min_v
            
            D_i = max(A_i, B_i)
            if D_i < ans:
                ans = D_i
        
        return ans
