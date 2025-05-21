class Solution:
    def asteroidsDestroyed(self, mass, asteroids):
        asteroids.sort()
        for a in asteroids:
            if mass < a:
                return False
            mass += a
        return True
