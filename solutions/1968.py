class Solution(object):
    def maxBuilding(self, n, restrictions):
        # add building 1 and n
        restrictions.append([1, 0])
        restrictions.append([n, n-1])
        # sort by position
        restrictions.sort(key=lambda x: x[0])
        m = len(restrictions)
        # forward pass
        for i in range(1, m):
            dist = restrictions[i][0] - restrictions[i-1][0]
            restrictions[i][1] = min(restrictions[i][1],
                                     restrictions[i-1][1] + dist)
        # backward pass
        for i in range(m-2, -1, -1):
            dist = restrictions[i+1][0] - restrictions[i][0]
            restrictions[i][1] = min(restrictions[i][1],
                                     restrictions[i+1][1] + dist)
        # compute maximum between adjacent restrictions
        ans = 0
        for i in range(1, m):
            id1, h1 = restrictions[i-1]
            id2, h2 = restrictions[i]
            d = id2 - id1
            # max height in this segment
            local_max = (h1 + h2 + d) // 2
            if local_max > ans:
                ans = local_max
        return ans
