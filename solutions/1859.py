class Solution:
    def minCharacters(self, a, b):
        # Count frequencies
        freqA = [0] * 26
        freqB = [0] * 26
        for ch in a:
            freqA[ord(ch) - 97] += 1
        for ch in b:
            freqB[ord(ch) - 97] += 1

        lenA, lenB = len(a), len(b)

        # Build prefix sums: prefixA[i] = count of letters <= i in a
        prefixA = [0] * 26
        prefixB = [0] * 26
        prefixA[0] = freqA[0]
        prefixB[0] = freqB[0]
        for i in range(1, 26):
            prefixA[i] = prefixA[i-1] + freqA[i]
            prefixB[i] = prefixB[i-1] + freqB[i]

        # Condition 1 & 2: pick boundary c from 1..25
        best = float('inf')
        for c in range(1, 26):
            # cond1: all a < all b by boundary c
            #   change a's letters >= c, change b's letters < c
            cost1 = (lenA - prefixA[c-1]) + prefixB[c-1]
            # cond2: all b < all a by boundary c
            cost2 = (lenB - prefixB[c-1]) + prefixA[c-1]
            best = min(best, cost1, cost2)

        # Condition 3: make both strings all one same letter
        for ch in range(26):
            # change everything in a and b not equal to ch
            cost3 = (lenA - freqA[ch]) + (lenB - freqB[ch])
            best = min(best, cost3)

        return best
