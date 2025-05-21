class Solution:
    def miceAndCheese(self, reward1, reward2, k):
        deltas = [(r1 - r2, r1, r2) for r1, r2 in zip(reward1, reward2)]
        # Sort by delta descending: biggest reward1 boost over reward2
        deltas.sort(reverse=True)

        total = 0
        for i in range(len(reward1)):
            if i < k:
                total += deltas[i][1]  # reward1
            else:
                total += deltas[i][2]  # reward2
        return total
