class Solution(object):
    def numberOfPairs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        ans = 0
        
        for i in range(n):
            ax, ay = points[i]
            for j in range(n):
                if i == j:
                    continue
                bx, by = points[j]
                
                # 1) Is A on the upper-left side of B (allowing horizontal/vertical lines)?
                if ax <= bx and ay >= by:
                    # 2) Check that no other point lies within the rectangle [ax..bx] Ã [by..ay]
                    ok = True
                    for k in range(n):
                        if k == i or k == j:
                            continue
                        xk, yk = points[k]
                        if ax <= xk <= bx and by <= yk <= ay:
                            ok = False
                            break
                    if ok:
                        ans += 1
        
        return ans
