class Solution(object):
    def reverseWords(self, s):
        # split on spaces, reverse each word, then rejoin
        return " ".join(word[::-1] for word in s.split(" "))
