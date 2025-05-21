class Encrypter(object):
    def __init__(self, keys, values, dictionary):
        # Map from char to its 2-letter encryption
        self.enc = {k: v for k, v in zip(keys, values)}
        # Precompute how many dictionary words encrypt to a given cipher
        self.count = {}
        for word in dictionary:
            e = self.encrypt(word)
            if e:
                self.count[e] = self.count.get(e, 0) + 1

    def encrypt(self, word1):
        res = []
        for c in word1:
            if c not in self.enc:
                return ""
            res.append(self.enc[c])
        return "".join(res)

    def decrypt(self, word2):
        return self.count.get(word2, 0)
