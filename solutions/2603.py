class Solution:
    def topStudents(self, positive_feedback, negative_feedback, report, student_id, k):
        pos = set(positive_feedback)
        neg = set(negative_feedback)
        score_map = {}

        for i in range(len(report)):
            score = 0
            for word in report[i].split():
                if word in pos:
                    score += 3
                elif word in neg:
                    score -= 1
            score_map[student_id[i]] = score

        return [sid for sid, _ in sorted(score_map.items(), key=lambda x: (-x[1], x[0]))[:k]]
