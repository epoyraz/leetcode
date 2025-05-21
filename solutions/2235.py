class Solution:
    def capitalizeTitle(self, title):
        words = title.split()
        for i in range(len(words)):
            if len(words[i]) <= 2:
                words[i] = words[i].lower()
            else:
                words[i] = words[i][0].upper() + words[i][1:].lower()
        return ' '.join(words)
