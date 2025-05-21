class Solution:
    def reorderLogFiles(self, logs):
        letter_logs = []
        digit_logs = []

        for log in logs:
            identifier, rest = log.split(" ", 1)
            if rest[0].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append((rest, identifier))

        # Sort letter logs: first by content, then by identifier
        letter_logs.sort()
        # Reconstruct the sorted letter logs
        sorted_letter_logs = [id_ + " " + content for content, id_ in letter_logs]

        return sorted_letter_logs + digit_logs
