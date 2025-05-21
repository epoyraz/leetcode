import collections

class Solution(object):
    def numMatchingSubseq(self, s, words):
        waiting = collections.defaultdict(list)
        for word in words:
            waiting[word[0]].append(iter(word[1:]))
        
        count = 0
        for c in s:
            advance = waiting.pop(c, [])
            for it in advance:
                nxt = next(it, None)
                if nxt:
                    waiting[nxt].append(it)
                else:
                    count += 1
        return count
