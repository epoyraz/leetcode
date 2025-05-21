class Solution:
    def sortTheStudents(self, score, k):
        return sorted(score, key=lambda row: row[k], reverse=True)
