class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict

        anagrams = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            anagrams[key].append(word)

        return list(anagrams.values())
