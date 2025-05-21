import heapq

class Solution:
    def kthSmallest(self, mat, k):
        m, n = len(mat), len(mat[0])
        # Priority queue to store the sums and the indices of elements from each row
        pq = [(sum(row[0] for row in mat), [0] * m)]  # Initial sum is the first element from each row
        visited = set(tuple([0] * m))  # To avoid revisiting the same index combination

        for _ in range(k):
            curr_sum, indices = heapq.heappop(pq)
            
            # Try all possible moves from the current indices
            for i in range(m):
                new_indices = list(indices)
                if new_indices[i] + 1 < n:
                    new_indices[i] += 1
                    new_tuple = tuple(new_indices)
                    if new_tuple not in visited:
                        visited.add(new_tuple)
                        new_sum = curr_sum - mat[i][indices[i]] + mat[i][new_indices[i]]
                        heapq.heappush(pq, (new_sum, new_indices))
        
        return curr_sum
