from collections import Counter

class Solution:
    def maxScoreWords(self, words, letters, score):
        letter_count = Counter(letters)

        def word_score(word):
            return sum(score[ord(c) - ord('a')] for c in word)

        def can_form(word, available):
            wc = Counter(word)
            for c in wc:
                if wc[c] > available[c]:
                    return False
            return True

        def backtrack(index, available):
            if index == len(words):
                return 0
            # Option 1: skip the word
            max_score = backtrack(index + 1, available)

            word = words[index]
            if can_form(word, available):
                used = Counter(word)
                for c in used:
                    available[c] -= used[c]
                total = word_score(word) + backtrack(index + 1, available)
                max_score = max(max_score, total)
                for c in used:
                    available[c] += used[c]

            return max_score

        return backtrack(0, letter_count)
