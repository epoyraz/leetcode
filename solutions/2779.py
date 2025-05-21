class Solution(object):
    def colorTheArray(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        colors = [0] * n
        same_adj = 0
        ans = []

        for idx, col in queries:
            old = colors[idx]
            # remove old adjacency contributions
            if old != 0:
                if idx > 0 and colors[idx - 1] == old:
                    same_adj -= 1
                if idx < n - 1 and colors[idx + 1] == old:
                    same_adj -= 1

            # assign new color
            colors[idx] = col

            # add new adjacency contributions
            if col != 0:
                if idx > 0 and colors[idx - 1] == col:
                    same_adj += 1
                if idx < n - 1 and colors[idx + 1] == col:
                    same_adj += 1

            ans.append(same_adj)

        return ans

# Example usage:
# sol = Solution()
# print(sol.colorTheArray(4, [[0,2],[1,2],[3,1],[1,1],[2,1]]))  # [0,1,1,0,2]
# print(sol.colorTheArray(1, [[0,100000]]))                   # [0]
