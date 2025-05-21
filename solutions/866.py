class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        return not (rec1[2] <= rec2[0] or  # rec1 right <= rec2 left
                    rec1[0] >= rec2[2] or  # rec1 left >= rec2 right
                    rec1[3] <= rec2[1] or  # rec1 top <= rec2 bottom
                    rec1[1] >= rec2[3])    # rec1 bottom >= rec2 top
