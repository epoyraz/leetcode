class Solution:
    def sortVowels(self, s):
        vowels = set('aeiouAEIOU')
        vlist = sorted([ch for ch in s if ch in vowels])
        res = []
        vi = 0
        for ch in s:
            if ch in vowels:
                res.append(vlist[vi])
                vi += 1
            else:
                res.append(ch)
        return ''.join(res)
