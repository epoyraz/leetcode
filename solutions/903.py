# Assume rand7() is already defined and returns a random integer from 1 to 7

class Solution:
    def rand10(self):
        while True:
            row = rand7()
            col = rand7()
            idx = (row - 1) * 7 + col  # maps to range 1 to 49
            if idx <= 40:
                return (idx - 1) % 10 + 1
