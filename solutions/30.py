class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        word_map = {}
        for word in words:
            word_map[word] = word_map.get(word, 0) + 1
        
        res = []
        
        for i in range(word_len):
            left = i
            right = i
            curr_map = {}
            count = 0

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word in word_map:
                    curr_map[word] = curr_map.get(word, 0) + 1
                    count += 1

                    while curr_map[word] > word_map[word]:
                        left_word = s[left:left + word_len]
                        curr_map[left_word] -= 1
                        left += word_len
                        count -= 1

                    if count == word_count:
                        res.append(left)
                else:
                    curr_map.clear()
                    count = 0
                    left = right
        
        return res
