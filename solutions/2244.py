class Solution:
    def numberOfBeams(self, bank):
        device_counts = [row.count('1') for row in bank if '1' in row]
        total = 0
        for i in range(1, len(device_counts)):
            total += device_counts[i - 1] * device_counts[i]
        return total
