class Solution(object):
    def bestRotation(self, nums):
        n = len(nums)
        diff = [0] * (n + 1)
        
        for i, num in enumerate(nums):
            low = (i + 1) % n
            high = (i - num + n + 1) % n
            diff[low] += 1
            diff[high] -= 1
            if low >= high:
                diff[0] += 1
        
        max_score = -1
        best_k = 0
        score = 0
        for k in range(n):
            score += diff[k]
            if score > max_score:
                max_score = score
                best_k = k
        return best_k
