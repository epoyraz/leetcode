class Solution(object):
    def findSecretWord(self, words, master):
        def match(a, b):
            return sum(x == y for x, y in zip(a, b))

        # Up to 30 guesses
        for _ in range(30):
            # Minimax selection
            best = None
            bestscore = float('inf')
            for w in words:
                cnt = [0] * 7
                for w2 in words:
                    if w2 != w:
                        cnt[match(w, w2)] += 1
                worst = max(cnt)
                if worst < bestscore:
                    bestscore = worst
                    best = w

            x = master.guess(best)
            if x == 6:
                return
            words = [w2 for w2 in words if match(best, w2) == x]
