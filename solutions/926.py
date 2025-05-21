class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        def encode(word):
            mapping = {}
            code = []
            next_code = 0
            for ch in word:
                if ch not in mapping:
                    mapping[ch] = next_code
                    next_code += 1
                code.append(mapping[ch])
            return code
        
        pattern_code = encode(pattern)
        return [word for word in words if encode(word) == pattern_code]
