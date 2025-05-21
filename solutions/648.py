class Solution(object):
    def replaceWords(self, dictionary, sentence):
        root_set = set(dictionary)
        words = sentence.split()
        res = []
        
        for word in words:
            prefix = ''
            for i in range(1, len(word)+1):
                if word[:i] in root_set:
                    prefix = word[:i]
                    break
            res.append(prefix if prefix else word)
        
        return ' '.join(res)
