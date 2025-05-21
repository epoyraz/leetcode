from collections import Counter

class Solution:
    def interchangeableRectangles(self, rectangles):
        def compute_gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        ratio_count = Counter()

        for w, h in rectangles:
            g = compute_gcd(w, h)
            ratio = (w // g, h // g)
            ratio_count[ratio] += 1

        total = 0
        for count in ratio_count.values():
            if count > 1:
                total += count * (count - 1) // 2

        return total
