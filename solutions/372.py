class Solution:
    def superPow(self, a, b):
        if not b:
            return 1
        last_digit = b.pop()
        part1 = pow(a, last_digit, 1337)
        part2 = pow(self.superPow(a, b), 10, 1337)
        return (part1 * part2) % 1337
