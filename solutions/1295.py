class Solution(object):
    def minimumPerimeter(self, neededApples):
        # Number of apples in a square of "radius" k is:
        #   A(k) = 2 * k * (k + 1) * (2*k + 1)
        def apples(k):
            return 2 * k * (k + 1) * (2 * k + 1)
        
        k = 0
        # increase k until we have enough apples
        while apples(k) < neededApples:
            k += 1
        # perimeter = 8 * k
        return 8 * k
