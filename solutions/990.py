class Solution:
    def isAlienSorted(self, words, order):
        index = {ch: i for i, ch in enumerate(order)}
        
        def in_order(w1, w2):
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    return index[c1] < index[c2]
            return len(w1) <= len(w2)
        
        for i in range(len(words) - 1):
            if not in_order(words[i], words[i + 1]):
                return False
        return True
