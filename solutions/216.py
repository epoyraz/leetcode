class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []

        def backtrack(start, path, target):
            if len(path) == k and target == 0:
                res.append(list(path))
                return
            if len(path) > k or target < 0:
                return
            for i in range(start, 10):
                path.append(i)
                backtrack(i + 1, path, target - i)
                path.pop()

        backtrack(1, [], n)
        return res
