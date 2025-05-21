class Solution:
    def mergeTriplets(self, triplets, target):
        seen = [False, False, False]

        for a, b, c in triplets:
            if a <= target[0] and b <= target[1] and c <= target[2]:
                if a == target[0]: seen[0] = True
                if b == target[1]: seen[1] = True
                if c == target[2]: seen[2] = True

        return all(seen)
