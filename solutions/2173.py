class Solution(object):
    def countValidWords(self, sentence):
        """
        :type sentence: str
        :rtype: int
        """
        def is_valid(tok):
            # Empty token not considered
            if not tok:
                return False

            hyphens = 0
            punctuations = 0
            n = len(tok)

            for i, ch in enumerate(tok):
                if ch.isdigit():
                    return False  # rule 1: no digits

                if ch == '-':
                    hyphens += 1
                    # rule 2: at most one, and must be surrounded by letters
                    if hyphens > 1:
                        return False
                    if i == 0 or i == n - 1:
                        return False
                    if not (tok[i-1].isalpha() and tok[i+1].isalpha()):
                        return False

                if ch in ('!', '.', ','):
                    punctuations += 1
                    # rule 3: at most one punctuation, and only at end
                    if punctuations > 1:
                        return False
                    if i != n - 1:
                        return False

                # letters are always fine

            return True

        tokens = sentence.split()
        count = 0
        for tok in tokens:
            if is_valid(tok):
                count += 1
        return count
