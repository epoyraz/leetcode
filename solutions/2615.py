from collections import Counter

class Solution:
    def isItPossible(self, word1, word2):
        c1 = Counter(word1)
        c2 = Counter(word2)

        for a in c1:
            for b in c2:
                # Clone counters to simulate the swap
                new_c1 = c1.copy()
                new_c2 = c2.copy()

                # Apply the swap a <-> b
                new_c1[a] -= 1
                if new_c1[a] == 0:
                    del new_c1[a]
                new_c2[b] -= 1
                if new_c2[b] == 0:
                    del new_c2[b]

                new_c1[b] = new_c1.get(b, 0) + 1
                new_c2[a] = new_c2.get(a, 0) + 1

                if len(new_c1) == len(new_c2):
                    return True

        return False
