import collections
import re

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        banned_set = set(banned)
        words = re.findall(r'\w+', paragraph.lower())
        count = collections.Counter(word for word in words if word not in banned_set)
        return count.most_common(1)[0][0]
