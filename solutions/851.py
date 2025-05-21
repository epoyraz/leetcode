class Solution(object):
    def toGoatLatin(self, sentence):
        vowels = set('aeiouAEIOU')
        words = sentence.split()
        res = []
        
        for i, word in enumerate(words):
            if word[0] in vowels:
                res.append(word + 'ma' + 'a' * (i + 1))
            else:
                res.append(word[1:] + word[0] + 'ma' + 'a' * (i + 1))
        
        return ' '.join(res)
