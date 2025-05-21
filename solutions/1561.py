class Solution(object):
    def arrangeWords(self, text):
        words = text.split(" ")
        # normalize to lowercase for sorting
        lower_words = [w.lower() for w in words]
        # stable sort by length
        sorted_words = sorted(lower_words, key=len)
        # capitalize first word, others remain lowercase
        sorted_words[0] = sorted_words[0].capitalize()
        return " ".join(sorted_words)
