class Solution:
    def spellchecker(self, wordlist, queries):
        vowels = set('aeiou')

        def devowel(word):
            return ''.join('*' if c in vowels else c for c in word)

        exact = set(wordlist)
        cap_map = {}
        vowel_map = {}

        for word in wordlist:
            low = word.lower()
            vow = devowel(low)
            if low not in cap_map:
                cap_map[low] = word
            if vow not in vowel_map:
                vowel_map[vow] = word

        result = []
        for q in queries:
            if q in exact:
                result.append(q)
            else:
                low = q.lower()
                vow = devowel(low)
                if low in cap_map:
                    result.append(cap_map[low])
                elif vow in vowel_map:
                    result.append(vowel_map[vow])
                else:
                    result.append("")

        return result
