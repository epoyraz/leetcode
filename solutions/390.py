class Solution:
    def lastRemaining(self, n):
        head = 1
        step = 1
        left_to_right = True
        
        while n > 1:
            if left_to_right or n % 2 == 1:
                head += step
            step *= 2
            n //= 2
            left_to_right = not left_to_right
        
        return head
