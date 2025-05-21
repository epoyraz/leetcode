class Solution:
    def pancakeSort(self, arr):
        res = []
        n = len(arr)
        
        for target in range(n, 1, -1):
            i = arr.index(target)
            if i == target - 1:
                continue
            if i != 0:
                res.append(i + 1)
                arr[:i + 1] = reversed(arr[:i + 1])
            res.append(target)
            arr[:target] = reversed(arr[:target])
        
        return res
