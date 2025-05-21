class Solution:
    def decrypt(self, code, k):
        n = len(code)
        res = [0] * n
        if k == 0:
            return res
        
        for i in range(n):
            s = 0
            if k > 0:
                for j in range(1, k+1):
                    s += code[(i + j) % n]
            else:  # k < 0
                for j in range(1, -k+1):
                    s += code[(i - j) % n]
            res[i] = s
        
        return res
