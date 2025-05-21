class Solution:
    def countEven(self, num):
        def digit_sum(n):
            return sum(int(d) for d in str(n))
        
        count = 0
        for i in range(1, num + 1):
            if digit_sum(i) % 2 == 0:
                count += 1
        return count
