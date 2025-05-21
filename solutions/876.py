from collections import Counter

class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        keys = sorted(count)
        
        for key in keys:
            while count[key] > 0:
                for i in range(groupSize):
                    if count[key + i] == 0:
                        return False
                    count[key + i] -= 1
        return True
