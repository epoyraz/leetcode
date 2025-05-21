class Solution(object):
    def judgePoint24(self, cards):
        def dfs(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6
            n = len(nums)
            for i in range(n):
                for j in range(n):
                    if i != j:
                        next_nums = []
                        for k in range(n):
                            if k != i and k != j:
                                next_nums.append(nums[k])
                        a, b = nums[i], nums[j]
                        for op in [a + b, a - b, b - a, a * b]:
                            next_nums.append(op)
                            if dfs(next_nums):
                                return True
                            next_nums.pop()
                        if abs(b) > 1e-6:
                            next_nums.append(a / b)
                            if dfs(next_nums):
                                return True
                            next_nums.pop()
                        if abs(a) > 1e-6:
                            next_nums.append(b / a)
                            if dfs(next_nums):
                                return True
                            next_nums.pop()
            return False
        
        return dfs(map(float, cards))
