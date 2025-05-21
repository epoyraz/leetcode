class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        word_set = set(wordDict)
        memo = {}

        def dfs(start):
            if start == len(s):
                return [""]  # Return list with empty string to start joining words

            if start in memo:
                return memo[start]

            sentences = []

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    for subsentence in dfs(end):
                        if subsentence:
                            sentences.append(word + " " + subsentence)
                        else:
                            sentences.append(word)

            memo[start] = sentences
            return sentences

        return dfs(0)
