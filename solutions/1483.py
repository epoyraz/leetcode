class Solution(object):
    def rankTeams(self, votes):
        if len(votes) == 1:
            return votes[0]

        n = len(votes[0])
        rank = {char: [0] * n for char in votes[0]}

        for vote in votes:
            for i, char in enumerate(vote):
                rank[char][i] -= 1  # negative for max-heap like sorting

        # Sort by rank values and then alphabetically
        return ''.join(sorted(votes[0], key=lambda x: (rank[x], x)))
